from pydantic import BaseModel


class CitySchema(BaseModel):
    name: str




class CityAddSchema(CitySchema):
    pass


class CityGetSchema(CitySchema):
    id:int
    pass

class CityUpdateSchema(CityGetSchema):
    pass