from typing import Any, Callable
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, PlainTextResponse


def create_exception_handler(
    status_code: int
) -> Callable[[Request, Exception], JSONResponse]:

    async def exception_handler(request: Request, exc: Exception):

        return JSONResponse(content=jsonable_encoder(exc), status_code=status_code)

    return exception_handler


def register_error_handlers(app: FastAPI):
    app.add_exception_handler(
        RequestValidationError,
        create_exception_handler(
            status_code=status.HTTP_403_FORBIDDEN,
        ),
    )
    app.add_exception_handler(
        IntegrityError,
        create_exception_handler(
            status_code=status.HTTP_400_BAD_REQUEST
        )
    )
    app.add_exception_handler(
        Exception,
        create_exception_handler(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    )
