from pydantic import BaseModel, conint
from typing import Any

# ! Get Grid Below
class GetGrid(BaseModel):
    gridName: str

class GetGridByID(BaseModel):
    gridID: int


# ! Get Grid Data Below
class Conditions(BaseModel):
    Attribute: str
    Values: list
    Operator: int

class Filter(BaseModel):
    Conditions: list[Conditions]

class Sort(BaseModel):
    Attribute: str
    Order: int

class GetGridData(BaseModel):
    GridID: int
    RecordCount: conint(ge=50)
    Filter: Filter
    StartIndex: conint(ge=1)
    Attributes: list[str]
    Sort: list[Sort]
    CustomSort: Any

class GetGridDataRoot(BaseModel):
    query: GetGridData


# ! Get User Settings Below
class GetUserSetting(BaseModel):
    settingName: str
