from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth import utils
from app.database import get_session
from app.schemas.user import UserGetSchema, UserUpdateActiveSchema, UserUpdateRoleSchema
from app.repositories.user import UserRepository

router_user = APIRouter(
    prefix="/users",
    tags=["user"]
)


@router_user.put("/{user_id}/active", status_code=status.HTTP_200_OK, response_model=UserGetSchema)
async def update_user_active(user_id: int,
                             data: UserUpdateActiveSchema,
                             _: None = Depends(utils.is_admin_access),
                             session: AsyncSession = Depends(get_session)):
    result = await UserRepository.update(user_id, data, session)
    return result


@router_user.put("/{user_id}/role", status_code=status.HTTP_200_OK, response_model=UserGetSchema)
async def update_user_role(user_id: int,
                           data: UserUpdateRoleSchema,
                           _: None = Depends(utils.is_admin_access),
                           session: AsyncSession = Depends(get_session)):
    result = await UserRepository.update(user_id, data, session)
    return result
