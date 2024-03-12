from fastapi import FastAPI, Depends, status, HTTPException, Query
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
import logging
from math import factorial
from starlette.responses import JSONResponse
from http import HTTPStatus
from datetime import datetime
from random import randint

app = FastAPI()

security = HTTPBasic()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
logger.addHandler(handler)


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "user"
    correct_password = "password"
    if credentials.username != correct_username or credentials.password != correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    return credentials.username


class Item(BaseModel):
    name: str
    description: str | None = None
    start_time: datetime | None = None
    end_time: datetime | None = None


@app.get("/get_items")
def get_items(username: str = Depends(get_current_username)) -> JSONResponse:
    logger.info(f'Trying to get items for user {username}')
    return JSONResponse(
        status_code=HTTPStatus.OK,
        content=Item(name='John', description='A very nice dog').dict()
    )


@app.post("/add_items")
def add_items(item: Item, username: str = Depends(get_current_username)) -> JSONResponse:
    logger.info(f'Added item: {item}')
    return JSONResponse(
        status_code=HTTPStatus.OK,
        content={"message": "Item added successfully", "id": randint(1, 9999)}
    )


@app.get("/factorial")
def get_factorial(num: int = Query(..., ge=0, le=100)) -> JSONResponse:
    logger.info(f'Trying to get factorial of {num}')
    result = factorial(num)
    return JSONResponse(
        status_code=HTTPStatus.OK,
        content={"result": str(result)}
    )
