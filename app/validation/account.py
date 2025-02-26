from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.bank import bankModel
from app.models.client import clientModel
from app.validation.general import ValidateServise

# эти функции вызываются для отдельных таблиц требующих своих определенных проверок.
# следовательно эта функция использует везде одну и ту же функцию для проверки наличия
# нужной нам информации в таблицах (передавая разные аргументы)


async def validateAccount(data: BaseModel, session: AsyncSession):
    return (data.balance >= 0
            # эта функция проверяет существует ли клиент с id равным data.client_id
            and await ValidateServise.validate_existence(clientModel, "client_id", data, session)
            and await ValidateServise.validate_existence(bankModel, "bank_id", data, session))
