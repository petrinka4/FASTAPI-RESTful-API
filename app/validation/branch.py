from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.bank import bankModel
from app.models.city import cityModel
from app.validation.general import ValidateServise


async def validateBranch(data: BaseModel, session: AsyncSession):
    return (await ValidateServise.validate_existence(cityModel, "city_id", data, session)
            and await ValidateServise.validate_existence(bankModel, "bank_id", data, session))
