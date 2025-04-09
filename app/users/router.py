from fastapi import APIRouter, HTTPException, status, Response, Query

from app.users.auth import get_password_hash, verify_password, authenticate_user, create_access_token
from app.users.repository import UserRepository
from app.users.schemas import SUserRegister

router = APIRouter(
    prefix="/user",
    tags=["Пользователи"]
)
# auth_router = APIRouter(
#     prefix="/auth",
#     tags=["Auth"]
# )
# router.include_router(auth_router)

@router.get('/is_user_exists')
async def is_user_exists(
        tg_id: int | None = Query(None, description="Telegram ID пользователя"),
        email: str | None = Query(None, description="Email пользователя")
):
    if tg_id:
        existing_user = await UserRepository.find_by_tg_id(tg_id)
    elif email:
        existing_user = await UserRepository.find_by_email(email)
    else:
        return {"error": "Укажите tg_id или email"}

    return {"result": existing_user is not None}

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