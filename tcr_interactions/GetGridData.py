import json

import requests
from common import headers

from tcr_interactions.get_grid import getGrid, getGridDataFields
from tcr_interactions.get_user_settings import getGridSortSettings
from tcr_interactions.post_models import GetGridDataModel, GetGridDataModelRoot

gridDataUrl = "http://apps.tcrsoftware.com/tcr_2/webservices/data.asmx/GetGridData"

def getGridData(Grid, FilterConditions, StartIndex=1, RecordCount=250):
    getGridInfo = getGrid(Grid)
    gridID = getGridInfo["GridID"]

    requestData = GetGridDataModelRoot(
        query=GetGridDataModel(
            GridID=gridID,
            RecordCount=RecordCount,
            Filter=FilterConditions,
            StartIndex=StartIndex,
            Attributes=getGridDataFields(gridID),
            Sort=[getGridSortSettings(gridID)],
            CustomSort=None,
        )
    ).json()
    response = requests.post(
        gridDataUrl, headers=headers, data=requestData).json()
    resultjson = json.loads(response["d"]["Result"])
    count = resultjson["RecordCount"]
    data = resultjson["Data"]
    return count, data
