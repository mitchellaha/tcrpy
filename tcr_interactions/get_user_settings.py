import json

import requests
from common import headers

from tcr_interactions.get_grid import getGrid, getGridByID
from tcr_interactions.post_models import GetUserSettingModel, SortModel

getUserSettingsURL = "https://apps.tcrsoftware.com/tcr_2/webservices/UserSettings.asmx/GetUserSetting"

def getUserSettings(settingName):
    """
    Gets The User Settings from TCR
        > SettingName is required
    """
    userSetting = GetUserSettingModel(settingName=settingName)
    response = requests.post(
        getUserSettingsURL, headers=headers, data=userSetting.json()).json()
    if isinstance(response["d"], str):
        responseLoad = json.loads(response["d"])
    else:
        responseLoad = response["d"]
    return responseLoad


def getGridSettings(grid):
    """
    Gets The Grid Settings from TCR
        > GridID or GridName is required
    """
    if isinstance(grid, str):
        gridNumber = getGrid(grid)["d"]["GridID"]
        gridSettingFormat = f"Yagna.Grid.{gridNumber}"
        gridSettings = getUserSettings(gridSettingFormat)
    if isinstance(grid, int):
        gridSettingFormat = f"Yagna.Grid.{grid}"
        gridSettings = getUserSettings(gridSettingFormat)
    return gridSettings


def getGridSortSettings(grid):
    """
    Gets the Grid Sort Settings if they Exist.
        > GridID or GridName is required
    """
    response = getGridSettings(grid)
    if response is not None:
        if response["SortDir"] == "sort-asc":
            sortDirINT = 1
        if response["SortDir"] == "sort-desc":
            sortDirINT = 0
        sort = SortModel(
            Attribute=response["SortCol"],
            Order=sortDirINT
        )
        return sort
    else:  # ? If there is no sort settings find the default sort settings
        getGridInfo = getGrid(grid)
        sort = SortModel(
            Attribute=getGridInfo["DefaultSortColumn"],
            Order=getGridInfo["DefaultSortOrder"])
        return sort
