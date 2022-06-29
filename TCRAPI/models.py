from typing import Any, List

from pydantic import BaseModel, conint
from typing import Optional, Union


# ! Get Grid Below
class GetGridModel(BaseModel):
    gridName: str

class GetGridByIDModel(BaseModel):
    gridID: int


# ! Get Grid Data Below
class FilterSearchConditionsModel(BaseModel):  # ! Used For Search
    Conditions: List
    GroupOperator: int
    Filter: Optional[Any]

class ConditionsModel(BaseModel):
    Attribute: str
    Values: List
    Operator: int

class FilterModel(BaseModel):
    Conditions: List[ConditionsModel]
    Filter: Optional[FilterSearchConditionsModel]


class SortModel(BaseModel):
    Attribute: str = None
    Order: int = 0

class GetGridDataModel(BaseModel):
    GridID: int
    RecordCount: conint(ge=50)
    Filter: Union[FilterModel, None]
    StartIndex: conint(ge=1)
    Attributes: List[str]
    Sort: List[SortModel]
    CustomSort: Any

class GetGridDataModelRoot(BaseModel):
    query: GetGridDataModel


class getTicketModel(BaseModel):
    ticketID: str

class getJobModel(BaseModel):
    JobID: str

class getCustomerModel(BaseModel):
    custID: str


# ! Get User Settings Below
class GetUserSettingModel(BaseModel):
    settingName: str
