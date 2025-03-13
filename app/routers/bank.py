
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.models.bank import bankModel
from app.schemas.bank import BankAddSchema
from app.resources.general import GeneralResources

router_bank = APIRouter(
    prefix="/banks",
    tags=["bank"]
)


@router_bank.post("")
async def create_bank(data: BankAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        result = await GeneralResources.create(bankModel, data, session)
        return {"status_code": 200, "object": result}
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))


# получение всех банков
@router_bank.get("")
async def get_banks(session: AsyncSession = Depends(get_session)):
    try:
        banks = await GeneralResources.get_all(bankModel, session)
        return banks
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))


# удаление банка по id
@router_bank.delete("/{bank_id}")
async def delete_bank(bank_id: int, session: AsyncSession = Depends(get_session)):
    try:
        await GeneralResources.delete(bank_id, bankModel, session)
        return {"status_code": 200, "message": "Deleted successfully"}
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))


# получение банка по id
@router_bank.get("/{bank_id}")
async def get_bank_by_id(bank_id: int, session: AsyncSession = Depends(get_session)):
    try:
        result = await GeneralResources.get_one(bank_id, bankModel, session)
        return result
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))

# апдейт банка по id


@router_bank.put("/{bank_id}")
async def update_bank_by_id(bank_id: int, data: BankAddSchema, session: AsyncSession = Depends(get_session)):
    try:
        result = await GeneralResources.update(bankModel, bank_id, data, session)
        return {"status_code": 201, "message": "Updated successfully", "object": result}
    except Exception as e:
        error_code = getattr(e, "status_code", 400)
        raise HTTPException(status_code=error_code, detail=str(e))
