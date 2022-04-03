from tcr_interactions.get_user_settings import getGridSortSettings
from tcr_interactions.get_grid import getGrid, getGridDataFields
from tcr_interactions.post_models import GetGridDataModelRoot, GetGridDataModel, SortModel, FilterModel, ConditionsModel
from common import headers, gridDataUrl
import requests
import json


def getGridData(Grid, FilterConditions, StartIndex=1, RecordCount=250):
    getGridInfo = getGrid(Grid)
    gridID = getGridInfo["GridID"]

    gridCustomSort = getGridSortSettings(gridID)
    if "SortCol" in gridCustomSort.keys():
        sort = SortModel(
            Attribute=gridCustomSort["SortCol"], Order=gridCustomSort["SorDirInt"])

    requestData = GetGridDataModelRoot(
        query=GetGridDataModel(
            GridID=gridID,
            RecordCount=RecordCount,
            Filter=FilterConditions,
            StartIndex=StartIndex,
            Attributes=getGridDataFields(gridID),
            Sort=[sort],
            CustomSort=None,
        )
    ).json()
    response = requests.post(
        gridDataUrl, headers=headers, data=requestData).json()
    resultjson = json.loads(response["d"]["Result"])
    count = resultjson["RecordCount"]
    data = resultjson["Data"]
    return count, data
