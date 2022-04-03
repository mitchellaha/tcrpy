from tcr_interactions.post_models import GetGrid, GetGridByID
from common import headers
import requests

getGridURL = "https://apps.tcrsoftware.com/tcr_2/webservices/config.asmx/GetGrid"
getGridByIDURL = "https://apps.tcrsoftware.com/tcr_2/webservices/config.asmx/GetGridByID"

def getGrid(gridName):
    """
    Gets The Full JSON Response from TCR with Grid Name
        > GridName is required
    """
    if isinstance(gridName, int):
        gridName = gridNameID(gridName)
    grid = GetGrid(gridName=gridName)
    response = requests.post(getGridURL, headers=headers, data=grid.json()).json()
    return response

def getGridByID(gridID):
    """
    Gets The Full JSON Response from TCR with Grid ID
        > GridID is required
    """
    if isinstance(gridID, str):
        gridID = gridNameID(gridID)
    grid = GetGridByID(gridID=gridID)
    response = requests.post(getGridByIDURL, headers=headers, data=grid.json()).json()
    return response

def gridNameID(grid):
    """
    If Given the GridName, Returns the GridID
    If Given the GridID, Returns the GridName
    """
    if isinstance(grid, str):
        grid = getGrid(grid)
        gridReturn = grid["d"]["GridID"]
    if isinstance(grid, int):
        grid = getGridByID(grid)
        gridReturn = grid["d"]["GridName"]
    return gridReturn

def getGridInfo(grid):
    """
    Gets The Relevant GridInfo from GridName
        > GridName is required
    """
    if grid is int:
        grid = gridNameID(grid)
    gridInfo = {}
    grid = getGrid(grid)
    gridInfo["GridTitle"] = grid["d"]["GridTitle"]
    gridInfo["GridName"] = grid["d"]["GridName"]
    gridInfo["GridID"] = grid["d"]["GridID"]
    gridInfo["PrimaryKeyField"] = grid["d"]["PrimaryKeyField"]
    gridInfo["EditURL"] = grid["d"]["EditURL"]
    gridInfo["FilterFields"] = grid["d"]["FilterFields"]
    gridInfo["Columns"] = grid["d"]["Columns"]
    return gridInfo


def getGridDataFields(grid):
    """
    Gets The Required Field Attributes from the Grid Name
    """
    gridData = getGrid(grid)
    dataFields = []
    for dField in gridData["d"]["Columns"]:
        dataFields.append(dField["DataField"])
    return dataFields

def getGridDataFieldsInfo(grid):
    """
    Gets The Fields with all info from the Grid Name
    """
    gridData = getGrid(grid)
    dataFields = []
    for dField in gridData["d"]["Columns"]:
        dataFields.append(dField)
    return dataFields

if __name__ == "__main__":
    # gridID = getGridByID(gridID=1)
    # print(gridID)

    # grid = getGrid("DRIVERSCHEDULE")
    # print(grid)

    # gridDataFields = getGridDataFields(54)
    # print(gridDataFields)


    # print(gridNameID(54))
    # print(gridNameID("DRIVERSCHEDULE"))

    # print(getGridName(54))
    # gridInfo = getGridInfo("DRIVERSCHEDULE")
    # print(gridInfo)

    # gridDataFieldsInfo = getGridDataFieldsInfo("DRIVERSCHEDULE")
    # print(gridDataFieldsInfo)

    pass
