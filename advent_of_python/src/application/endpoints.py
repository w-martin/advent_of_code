from enum import Enum

from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter
from fastapi.params import Depends
from starlette.requests import Request
from starlette.responses import Response

from model.factory import Factory
from model.transformer import Transformer

router = APIRouter()


class Part(Enum):
    one = "1"
    two = "2"


@router.post("/day/{day}/part/{part}", response_class=Response)
@inject
async def process_request(
        day: str,
        part: Part,
        request: Request,
        transformer_factory: Factory[Transformer] = Depends(Provide[Factory[Transformer]])
):
    transformer = transformer_factory.new(day)
    data: str = (await request.body()).decode("utf-8")
    result = ""
    match part:
        case Part.one:
            result = transformer.transform_1(data)
        case Part.two:
            result = transformer.transform_2(data)
    return str(result)
