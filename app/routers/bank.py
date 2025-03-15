
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_session
from app.schemas.bank import BankAddSchema
from app.repositories.bank import BankRepository

router_bank = APIRouter(
    prefix="/banks",
    tags=["bank"]
)


@router_bank.post("", status_code=status.HTTP_201_CREATED)
async def create_bank(data: BankAddSchema, session: AsyncSession = Depends(get_session)):
    result = await BankRepository.create(data, session)
    return {"object": result}


# получение всех банков
@router_bank.get("", status_code=status.HTTP_200_OK)
async def get_banks(session: AsyncSession = Depends(get_session)):
    banks = await BankRepository.get_all(session)
    return banks


# удаление банка по id
@router_bank.delete("/{bank_id}", status_code=status.HTTP_200_OK)
async def delete_bank(bank_id: int, session: AsyncSession = Depends(get_session)):
    await BankRepository.delete(bank_id,  session)
    return {"message": "Deleted successfully"}


# получение банка по id
@router_bank.get("/{bank_id}", status_code=status.HTTP_200_OK)
async def get_bank_by_id(bank_id: int, session: AsyncSession = Depends(get_session)):
    result = await BankRepository.get_one(bank_id,  session)
    return result

# апдейт банка по id


@router_bank.put("/{bank_id}", status_code=status.HTTP_200_OK)
async def update_bank_by_id(bank_id: int, data: BankAddSchema, session: AsyncSession = Depends(get_session)):
    result = await BankRepository.update(bank_id, data, session)
    return {"object": result}
