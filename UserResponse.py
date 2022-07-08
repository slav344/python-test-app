from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class InfoResponse:
    seed: str
    results: int
    page: int
    version: str


@dataclass_json
@dataclass
class NameResponse:
    title: str
    first: str
    last: str


# @dataclass_json
# @dataclass
# class IdResponse:
#     name: str
#     value: str


@dataclass_json
@dataclass
class ResultResponse:
    # id: IdResponse
    gender: str
    name: NameResponse
    email: str
    phone: str


@dataclass_json
@dataclass
class UserResponse:
    info: InfoResponse
    results: List[ResultResponse]
