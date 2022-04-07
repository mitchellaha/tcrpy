import requests
from tcr_interactions.main import headers

from tcr_interactions.post_models import GetGridByIDModel, GetGridModel

getGridURL = "https://apps.tcrsoftware.com/tcr_2/webservices/config.asmx/GetGrid"
getGridByIDURL = "https://apps.tcrsoftware.com/tcr_2/webservices/config.asmx/GetGridByID"

def getGrid(gridName):
    """
    Gets The Full JSON Response from TCR with Grid Name
        > GridName is required
    """
    if isinstance(gridName, int):
        gridName = gridNameID(gridName)
    grid = GetGridModel(gridName=gridName)
    response = requests.post(getGridURL, headers=headers, data=grid.json()).json()
    data = response["d"]
    return data

def getGridByID(gridID):
    """
    Gets The Full JSON Response from TCR with Grid ID
        > GridID is required
    """
    if isinstance(gridID, str):
        gridID = gridNameID(gridID)
    grid = GetGridByIDModel(gridID=gridID)
    response = requests.post(getGridByIDURL, headers=headers, data=grid.json()).json()
    data = response["d"]
    return data

def gridNameID(grid):
    """
    If Given the GridName, Returns the GridID
    If Given the GridID, Returns the GridName
    """
    if isinstance(grid, str):
        grid = getGrid(grid)
        gridReturn = grid["GridID"]
    if isinstance(grid, int):
        grid = getGridByID(grid)
        gridReturn = grid["GridName"]
    return gridReturn

def getGridInfo(grid):
    """
    Gets The Relevant GridInfo from GridName
        > GridName is required
    """
    gridInfo = {}
    grid = getGrid(grid)
    gridInfo["GridTitle"] = grid["GridTitle"]
    gridInfo["GridName"] = grid["GridName"]
    gridInfo["GridID"] = grid["GridID"]
    gridInfo["PrimaryKeyField"] = grid["PrimaryKeyField"]
    gridInfo["EditURL"] = grid["EditURL"]
    gridInfo["FilterFields"] = grid["FilterFields"]
    gridInfo["Columns"] = grid["Columns"]
    return gridInfo


def getGridDataFields(grid):
    """
    Gets The Required Field Attributes from the Grid Name
        > GridName is required
    """
    gridData = getGrid(grid)
    dataFields = []
    for dField in gridData["Columns"]:
        dataFields.append(dField["DataField"])
    return dataFields

def getGridDataFieldsInfo(grid):
    """
    Gets The Fields with all info from the Grid Name
        > GridName is required
    """
    gridData = getGrid(grid)
    dataFields = []
    for dField in gridData["Columns"]:
        dataFields.append(dField)
    return dataFields

def getGridQuickSearchFields(grid):
    """
    Gets The QuickSearch Fields from the Grid Name
        > GridName is required
    """
    gridFields = getGridDataFieldsInfo(grid)
    quickSearchFields = []
    for field in gridFields:
        if field["QuickSearch"] is True:
            quickSearchFields.append(field["DataField"])
    return quickSearchFields
