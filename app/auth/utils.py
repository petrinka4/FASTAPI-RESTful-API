from datetime import datetime, timedelta
import bcrypt
import jwt
from sqlalchemy import select
from app.config import settings
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, status

from app.database import get_session
from app.models.user import userModel

http_bearer = HTTPBearer()

allowed_admin = ["admin"]
allowed_edit = ["admin", "editor"]
allowed_read = allowed_edit.copy()
allowed_read.append("user")


def encode_jwt(
        payload: dict,
        expire_minutes: int,
        private_key: str = settings.auth_jwt.private_key_path.read_text(),
        algorythm: str = settings.auth_jwt.algorithm,

):
    to_encode = payload.copy()
    now = datetime.utcnow()
    expire = now + timedelta(minutes=expire_minutes)
    to_encode.update(
        exp=expire,
        iat=now
    )
    encoded = jwt.encode(
        payload=to_encode, key=private_key, algorithm=algorythm)
    return encoded


def decode_jwt(token: str | bytes,
               public_key: str = settings.auth_jwt.public_key_path.read_text(),
               algorithm: str = settings.auth_jwt.algorithm,):
    try:
        decoded = jwt.decode(token, public_key, algorithms=[algorithm])
        return decoded
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired. Please refresh your token."
        )
    except jwt.DecodeError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid token."
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred: {str(e)}"
        )


def hash_password(
        password: str
) -> bytes:
    salt = bcrypt.gensalt()
    pwd_bytes: bytes = password.encode()
    return bcrypt.hashpw(pwd_bytes, salt)


def validate_password(
        password: str,
        hash_password: bytes
):
    return bcrypt.checkpw(password.encode(), hash_password)


async def get_user_role_by_username(username: str, session: AsyncSession):
    query = select(userModel).filter(userModel.username == username)
    result = await session.execute(query)
    user = result.scalar()

    if user:
        role = user.role.name if user.role else None
        return role
    return None


async def get_user_active_by_username(username: str, session: AsyncSession):
    query = select(userModel).filter(userModel.username == username)
    result = await session.execute(query)
    user = result.scalar()

    if user:
        active = user.active
        return active
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


def get_user_from_jwt_refresh(credentials: HTTPAuthorizationCredentials = Depends(http_bearer)):
    token = credentials.credentials
    decoded_data = decode_jwt(token)
    if decoded_data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    type = decoded_data.get("type")
    if type != "refresh":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token type")
    username = decoded_data.get("username")
    if username == None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    return username


async def is_admin_access(credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
                          session: AsyncSession = Depends(get_session)):
    token = credentials.credentials
    decoded_data = decode_jwt(token)
    if decoded_data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    type = decoded_data.get("type")
    if type != "access":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token type")
    
    username = decoded_data.get("username")
    active = await get_user_active_by_username(username,session)
    if active != True:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="User inactive")
    role = decoded_data.get("role")
    if role not in allowed_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")
    return


async def is_editor_access(credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
                           session: AsyncSession = Depends(get_session)):
    token = credentials.credentials
    decoded_data = decode_jwt(token)
    if decoded_data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    type = decoded_data.get("type")
    if type != "access":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token type")
    username = decoded_data.get("username")
    active = await get_user_active_by_username(username,session)
    if active != True:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="User inactive")

    role = decoded_data.get("role")
    if role not in allowed_edit:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")
    return


async def is_user_access(credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
                         session: AsyncSession = Depends(get_session)):
    token = credentials.credentials
    decoded_data = decode_jwt(token)
    if decoded_data is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    type = decoded_data.get("type")
    if type != "access":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token type")
    username = decoded_data.get("username")
    active = await get_user_active_by_username(username,session)
    if active != True:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="User inactive")
    role = decoded_data.get("role")
    if role not in allowed_read:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")
    return
