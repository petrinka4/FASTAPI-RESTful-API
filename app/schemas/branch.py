from pydantic import BaseModel


class BranchSchema(BaseModel):
    bank_id: int
    city_id: int




class BranchAddSchema(BranchSchema):
    pass


class BranchGetSchema(BranchSchema):
    id:int
    pass

class BranchUpdateSchema(BranchGetSchema):
    pass