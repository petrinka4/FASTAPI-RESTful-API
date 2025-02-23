from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.account import accountModel
from app.validation.general import ValidateServise


async def validateCard(data: BaseModel, session: AsyncSession):
    return (await ValidateServise.validate_existence(accountModel, "account_id", data, session))
