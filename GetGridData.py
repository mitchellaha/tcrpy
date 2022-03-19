from pydantic import BaseModel, conint


class Conditions(BaseModel):
    Attribute: str
    Values: list
    Operator: int


class Filter(BaseModel):
    Conditions: list[Conditions]


class Sort(BaseModel):
    Attribute: str
    Order: int


class Query(BaseModel):
    GridID: int
    RecordCount: int
    Filter: Filter
    StartIndex: conint(ge=1)
    Attributes: list[str]
    Sort: list[Sort]
    CustomSort: None


class Root(BaseModel):
    query: Query


QueryParamOperator = {
    "Equal": 1,
    "NotEqual": 2,
    "LessThan": 3,
    "LessThanOrEqual": 4,
    "GreaterThan": 5,
    "GreaterThanOrEqual": 6,
    "Between": 7,
    "StartsWith": 8,
    "EndsWith": 9,
    "Contains": 10,
    "NotContains": 11,
    "OneOf": 12,
    "NotOneOf": 13,
    "IsNull": 14,
    "NotNull": 15
}

QuerySort = {
    "ASC": 0,
    "DESC": 1
}
QueryGroupOperator = {
    "AND": 1,
    "OR": 2
}

GridType = {
    "TCRGrid": 1,
    "FindGrid": 2,
    "QuickView": 3,
    "SubTCRGrid": 4
}

QueryFilterFieldDataType = {
    "None": 0,
    "ID": 1,
    "Money": 2,
    "Text": 3,
    "Date": 4,
    "CheckboxRadio": 5,
    "Lookup": 6,
    "Number": 7
}

Entity = {
    "Customer": 1,
    "Job": 2,
    "Ticket": 3,
    "Invoice": 8,
    "Quote": 9,
    "Activity": 12
}

TabType = {
    "Card": 1,
    "Grid": 2,
    "Url": 3
}

GridFilterDataType = {
    "Text": 1,
    "Date": 2,
    "Number": 3,
    "PickList": 4,
    "Lookup": 5,
    "MultiLabels": 6
}
