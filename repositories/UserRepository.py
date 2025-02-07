import secrets
from database import db
from models.UserModel import User
from schemas.UserSchema import UserCreate
from sqlalchemy.future import select
from utils.email import send_reset_email




async def request_password_reset(email: str):
    query = select(User).where(User.email == email)
    result = await db.execute(query)
    user = result.scalar_one_or_none()

    if not user:
        return {"message": "User not found"}

    # Gerar token seguro
    reset_token = secrets.token_urlsafe(32)
    user.reset_token = reset_token
    await db.commit()

    # Aqui você deve enviar um e-mail ao usuário com um link contendo o token
    #print(f"Recuperação de senha: use este token {reset_token}")

     # Enviar email
    await send_reset_email(user.email, reset_token)

    return {"message": "Password reset link sent to your email"}


async def reset_password(token: str, new_password: str):
    query = select(User).where(User.reset_token == token)
    result = await db.execute(query)
    user = result.scalar_one_or_none()

    if not user:
        return {"message": "Invalid or expired token"}

    user.password = new_password  # Em produção, você deve hashear a senha
    user.reset_token = None  # Apagar o token após a redefinição
    await db.commit()

    return {"message": "Password reset successfully"}


# R READ
async def get_all():
    query = select(User)
    result = await db.execute(query)
    return result.scalars().all()
   

# U UPDATE
async def update(user_id: int, request_body: UserCreate):
    query = await db.get(User, user_id)
    if not query:
        return {"message": "User not found"}
    else:
        query.name = request_body.name
        query.email = request_body.email
        query.password = request_body.password
        await db.commit()
        return query

# D DELETE
async def delete(user_id: int):
    user = await db.get(User, user_id)
    if not user:
        return {"message": "User not found"}
    await db.delete(user)
    await db.commit()
    return {"message": "User deleted successfully"}
