from fastapi import APIRouter, HTTPException
from repositories import UserRepository
from schemas.UserSchema import UserCreate, UserResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

# CREATE
@router.post("/", response_model= UserResponse)
async def create_user(request_body: UserCreate):
    return await UserRepository.create(request_body)

# READ
@router.get("/", response_model=list[UserResponse])
async def get_all_user():
    return await UserRepository.get_all()

# UPDATE
@router.put("/{user_id}", response_model=UserResponse | dict)
async def update_user(user_id: int, request_body: UserCreate):
    return await UserRepository.update(user_id, request_body)

# DELETE
@router.delete("/{user_id}")
async def delete_user(user_id: int):
    return await UserRepository.delete(user_id)
    