from tcr_interactions.post_models import GetUserSettingModel, SortModel
from tcr_interactions.get_grid import getGrid, getGridByID
from common import headers
import requests
import json

getUserSettingsURL = "https://apps.tcrsoftware.com/tcr_2/webservices/UserSettings.asmx/GetUserSetting"

def getUserSettings(settingName):
    """
    Gets The User Settings from TCR
        > SettingName is required
    """
    userSetting = GetUserSettingModel(settingName=settingName)
    response = requests.post(getUserSettingsURL, headers=headers, data=userSetting.json()).json()
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
    if "SortCol" in response.keys():
        sort = {}
        sort["SortCol"] = response["SortCol"]
        sort["SortDir"] = response["SortDir"]
        if response["SortDir"] == "sort-asc":
            sort["SorDirInt"] = 1
        if response["SortDir"] == "sort-desc":
            sort["SorDirInt"] = 0
        return sort
    # resp = Sort(Attribute=sort["SortCol"], Order=sort["SorDirInt"])
    # return resp

if __name__ == "__main__":
    # print(getUserSettings("Yagna.Grid.10"))
    # print(getGridSettings(1))
    print(getGridSettings("DRIVERSCHEDULE"))
    # print(getGridSortSettings("DRIVERSCHEDULE"))
