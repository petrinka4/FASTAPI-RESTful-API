from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models.social_status import social_statusModel
from app.schemas.social_status import Social_StatusAddSchema
from app.resources.general import GeneralResources

router_status = APIRouter(
    prefix="/social_status",
    tags=["status"]
)

# добавление статуса


@router_status.post("")
async def create_status(data: Social_StatusAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        result = await GeneralResources.create(social_statusModel, data, session)
        return {"status_code": 200, "object": result}
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))


# получение всех статусов
@router_status.get("")
async def get_statuses(session: AsyncSession = Depends(get_session)):
    try:
        statuses = await GeneralResources.get_all(social_statusModel, session)
        return statuses
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))


# удаление статуса по id
@router_status.delete("/{status_id}")
async def delete_status(status_id: int, session: AsyncSession = Depends(get_session)):
    try:
        await GeneralResources.delete(status_id, social_statusModel, session)
        return {"status_code": 200, "message": "Deleted successfully"}
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))


# получение статуса по id
@router_status.get("/{status_id}")
async def get_status_by_id(status_id: int, session: AsyncSession = Depends(get_session)):
    try:
        result = await GeneralResources.get_one(status_id, social_statusModel, session)
        return result
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))

# апдейт статуса по id


@router_status.put("/{status_id}")
async def update_status_by_id(status_id: int, data: Social_StatusAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        result = await GeneralResources.update(social_statusModel, status_id, data, session)
        return {"status_code": 201, "message": "Updated successfully", "object": result}
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))
