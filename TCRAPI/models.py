from typing import Any

from pydantic import BaseModel, conint


# ! Get Grid Below
class GetGridModel(BaseModel):
    gridName: str

class GetGridByIDModel(BaseModel):
    gridID: int


# ! Get Grid Data Below
class ConditionsModel(BaseModel):
    Attribute: str
    Values: list
    Operator: int

class FilterModel(BaseModel):
    Conditions: list[ConditionsModel]

class FilterSearchConditionsModel(BaseModel):  # ! Used For Search
    Conditions: list
    GroupOperator: int

class FilterSearchModel(BaseModel):  # ! Used For Search
    Conditions: list
    Filter: FilterSearchConditionsModel

class SortModel(BaseModel):
    Attribute: str = None
    Order: int = 0

class GetGridDataModel(BaseModel):
    GridID: int
    RecordCount: conint(ge=50)
    Filter: Any
    StartIndex: conint(ge=1)
    Attributes: list[str]
    Sort: list[SortModel]
    CustomSort: Any

class GetGridDataModelRoot(BaseModel):
    query: GetGridDataModel


# ! Get User Settings Below
class GetUserSettingModel(BaseModel):
    settingName: str
