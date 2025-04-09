from typing import List
from fastapi import APIRouter, Depends, Form, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models.user import userModel
from app.schemas.token import TokenInfo
from app.schemas.user import UserAddSchema, UserLoginSchema, UserGetSchema
import app.auth.utils as utils
from app.config import settings


router = APIRouter(prefix="/auth", tags=["JWT"])


@router.post("/signup",status_code=status.HTTP_201_CREATED,response_model=UserGetSchema)
async def singup(data: UserAddSchema, session: AsyncSession = Depends(get_session)):
    hashed_password = utils.hash_password(data.password)
    data = data.model_dump()
    data["password"] = hashed_password
    data.setdefault("role_id", 3)
    obj = userModel(**data)
    session.add(obj)
    await session.commit()
    return obj

# тестовая ручка для получения всех юзеров(может только админ)


@router.get("/signup",status_code=status.HTTP_201_CREATED,response_model=List[UserGetSchema])
async def get_users(session: AsyncSession = Depends(get_session),
                    _: None = Depends(utils.is_admin_access)):
    query = select(userModel)
    users = await session.scalars(query)
    return users.all()


async def validate_auth_user(
    session: AsyncSession = Depends(get_session),
    username: str = Form(...),
    password: str = Form(...)
):
    unauthed_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password"
    )

    result = await session.execute(select(userModel).where(userModel.username == username))
    user = result.scalars().first()

    if not user:
        raise unauthed_exc
    if not utils.validate_password(password=password, hash_password=user.password):
        raise unauthed_exc

    return user


@router.post("/login", response_model=TokenInfo)
async def login(session: AsyncSession = Depends(get_session), user: UserLoginSchema = Depends(validate_auth_user)):
    role = await utils.get_user_role_by_username(user.username, session)

    jwt_payload_access = {
        "type": "access",
        "sub": user.username,
        "username": user.username,
        "role": role
    }
    jwt_payload_refresh = {
        "type": "refresh",
        "sub": user.username,
        "username": user.username
    }
    access_token = utils.encode_jwt(
        payload=jwt_payload_access, expire_minutes=settings.auth_jwt.access_token_expire_minutes)
    refresh_token = utils.encode_jwt(
        payload=jwt_payload_refresh, expire_minutes=settings.auth_jwt.refresh_token_expire_minutes)
    return TokenInfo(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="Bearer"
    )


@router.post("/refresh", response_model=TokenInfo, response_model_exclude_none=True)
async def auth_refresh_jwt(session: AsyncSession = Depends(get_session), username: str = Depends(utils.get_user_from_jwt_refresh)):

    role = await utils.get_user_role_by_username(username, session)

    jwt_payload_access = {
        "type": "access",
        "sub": username,
        "username": username,
        "role": role
    }

    access_token = utils.encode_jwt(
        payload=jwt_payload_access, expire_minutes=settings.auth_jwt.access_token_expire_minutes)
    return TokenInfo(
        access_token=access_token,
        token_type="Bearer"
    )

