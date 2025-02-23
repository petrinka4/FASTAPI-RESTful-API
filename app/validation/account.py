from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.bank import bankModel
from app.models.client import clientModel
from app.validation.general import ValidateServise


async def validateAccount(data: BaseModel, session: AsyncSession):
    return (await ValidateServise.validate_existence(clientModel, "client_id", data, session) and await ValidateServise.validate_existence(bankModel, "bank_id", data, session))
