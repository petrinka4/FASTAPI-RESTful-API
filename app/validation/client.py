from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.social_status import social_statusModel
from app.validation.general import ValidateServise


async def validateClient(data: BaseModel, session: AsyncSession):
    return (await ValidateServise.validate_existence(social_statusModel, "social_status_id", data, session))
