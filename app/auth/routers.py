from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models.user import userModel
from app.schemas.token import AccessTokenPayloadSchema, RefreshTokenPayloadSchema, TokenInfo
from app.schemas.user import UserAddSchema, UserLoginSchema, UserGetSchema
import app.auth.utils as utils
from app.config import settings


router = APIRouter(prefix="/auth", tags=["JWT"])


@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=UserGetSchema)
async def singup(data: UserAddSchema, session: AsyncSession = Depends(get_session)):
    data = data.model_dump()
    data.setdefault("role_id", 3)
    obj = userModel(**data)
    session.add(obj)
    await session.commit()
    return obj

# тестовая ручка для получения всех юзеров(может только админ)


@router.get("/users", status_code=status.HTTP_201_CREATED, response_model=List[UserGetSchema])
async def get_users(session: AsyncSession = Depends(get_session),
                    _: bool = utils.role_required(["admin", "editor"])):
    query = select(userModel)
    users = await session.scalars(query)
    return users.all()


@router.post("/login", response_model=TokenInfo)
async def login(session: AsyncSession = Depends(get_session), user: UserLoginSchema = Depends(utils.validate_auth_user)):
    role = await utils.get_user_role_by_username(user.username, session)

    access_payload = AccessTokenPayloadSchema(
        sub=user.username,
        username=user.username,
        role=role
    )

    refresh_payload = RefreshTokenPayloadSchema(
        sub=user.username,
        username=user.username
    )

    access_token = utils.encode_jwt(
        payload=access_payload.model_dump(),
        expire_minutes=settings.auth_jwt.access_token_expire_minutes
    )

    refresh_token = utils.encode_jwt(
        payload=refresh_payload.model_dump(),
        expire_minutes=settings.auth_jwt.refresh_token_expire_minutes
    )
    return TokenInfo(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="Bearer"
    )


@router.post("/refresh", response_model=TokenInfo)
async def auth_refresh_jwt(session: AsyncSession = Depends(get_session),
                           payload: str = Depends(utils.validate_refresh_token)):

    username = payload.get("username")
    role = await utils.get_user_role_by_username(username, session)

    access_payload = AccessTokenPayloadSchema(
        sub=username,
        username=username,
        role=role
    )

    refresh_payload = RefreshTokenPayloadSchema(
        sub=username,
        username=username
    )
    access_token = utils.encode_jwt(
        payload=access_payload.model_dump(),
          expire_minutes=settings.auth_jwt.access_token_expire_minutes)
    
    refresh_token = utils.encode_jwt(
        payload=refresh_payload.model_dump(),
        expire_minutes=settings.auth_jwt.refresh_token_expire_minutes
    )

    return TokenInfo(
        access_token=access_token,
        refresh_token=refresh_token,
        token_type="Bearer"
    )
