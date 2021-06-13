from fastapi import FastAPI

from pydantic import BaseModel, conint

app = FastAPI()


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
