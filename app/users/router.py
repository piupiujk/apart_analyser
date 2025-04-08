from fastapi import APIRouter, HTTPException, status, Response

from app.users.auth import get_password_hash, verify_password, authenticate_user, create_access_token
from app.users.repository import UserRepository
from app.users.schemas import SUserRegister

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"]
)

@router.post('/register')
async def register_user(user_data: SUserRegister):
    existing_user = await UserRepository.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(
            status_code=400,
        )
    hashed_password = get_password_hash(user_data.password)
    await UserRepository.add_user(email=user_data.email, password=hashed_password)

@router.post('/login')
async def login_user(response: Response, user_data: SUserRegister):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token({'sub': user.id})
    response.set_cookie('apartment_access_token', access_token, httponly=True)
    return access_token


@router.get('/is_user_exists')
async def is_user_exists(tg_id: int):
    existing_user = await UserRepository.find_by_tg_id(tg_id=tg_id)
    return {"result": existing_user is not None}

# @router.post('/add_tg_id')
# async def add_tg_id(email: str, tg_id: str):
#     existing_user = await UserRepository.find_one_or_none(email=email)
#     if not existing_user:
#         raise HTTPException()
#     if existing_user.tg_id:
#         raise HTTPException()
#     existing_user.tg_id = tg_id
#     return 'Добавлено'