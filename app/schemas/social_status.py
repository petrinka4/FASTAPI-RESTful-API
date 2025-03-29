from pydantic import BaseModel


class Social_StatusSchema(BaseModel):
    name: str



class Social_StatusAddSchema(Social_StatusSchema):
    pass


class Social_StatusGetSchema(Social_StatusSchema):
    id:int
    pass

class Social_StatusUpdateSchema(Social_StatusGetSchema):
    pass