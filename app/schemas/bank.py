from pydantic import BaseModel


class BankSchema(BaseModel):
    name: str


class BankAddSchema(BankSchema):
    pass


class BankGetSchema(BankSchema):
    id:int
    pass

class BankUpdateSchema(BankGetSchema):
    pass