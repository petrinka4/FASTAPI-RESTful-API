from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models.social_status import social_statusModel
from app.schemas import Social_StatusAddSchema
from app.resources.social_status import StatusResources
from app.resources.general import GeneralResources

router_status = APIRouter(
    prefix="/social_status",
    tags=["status"]
)

# добавление статуса


@router_status.post("")
async def add_status(data: Social_StatusAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        result = await StatusResources.add_status(data, session)
        return {"status_code": 200, "object": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")


# получение всех статусов
@router_status.get("")
async def get_statuses(session: AsyncSession = Depends(get_session)):
    statuses = await GeneralResources.get_all(social_statusModel, session)
    return statuses


# удаление статуса по id
@router_status.delete("/{status_id}")
async def delete_status(status_id: int, session: AsyncSession = Depends(get_session)):
    try:
        await GeneralResources.delete_one(status_id, social_statusModel, session)
        return {"status_code": 200, "message": "Deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error: {str(e)}")


# получение статуса по id
@router_status.get("/{status_id}")
async def get_status_by_id(status_id: int, session: AsyncSession = Depends(get_session)):
    try:
        result = await GeneralResources.get_one(status_id, social_statusModel, session)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error: {str(e)}")

# апдейт статуса по id


@router_status.put("/{status_id}")
async def update_status_by_id(status_id: int, data: Social_StatusAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        await StatusResources.update_status(status_id, data, session)
        return {"status_code": 200, "message": "Updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error: {str(e)}")
