from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr
import os
from pydantic_settings import BaseSettings

class EmailConfig(BaseSettings):
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_SERVER: str
    MAIL_PORT: int
    MAIL_FROM: str
    USE_CREDENTIALS: bool
    MAIL_STARTTLS: bool
    MAIL_SSL_TLS: bool

    class Config:
        env_file = ".env"

conf = EmailConfig()

async def send_reset_email(email: EmailStr, token: str):
    reset_link = f"http://localhost:8000/reset-password?token={token}"
    message = MessageSchema(
        subject="Redefinição de Senha",
        recipients=[email],
        body=f"Clique no link para redefinir sua senha: {reset_link}",
        subtype="html"
    )
    fm = FastMail(conf)
    await fm.send_message(message)
