import uvicorn
from fastapi import FastAPI

from pydantic import BaseModel, conint
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins='*',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class InputData(BaseModel):
    number1: conint(strict=True, gt=0)
    number2: conint(strict=True, ge=0)


class Result(BaseModel):
    result: conint(strict=True, gt=0)


def my_sum(number1, number2):
    return number1 + number2


@app.post("/calc", response_model=Result)
def calc(input_data: InputData):
    result = my_sum(input_data.number1, input_data.number2)
    return Result(result=result)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
