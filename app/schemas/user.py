from pydantic import BaseModel, ConfigDict


class UserSchema(BaseModel):
    model_config = ConfigDict(strict=True)
    username: str
    active: bool = True


class UserGetSchema(UserSchema):
    role_id: int


class UserAddSchema(UserSchema):
    password: str


class UserUpdateRoleSchema(BaseModel):
    role_id: int


class UserUpdateActiveSchema(BaseModel):
    active: bool


class UserLoginSchema(BaseModel):
    username: str
    password: str
