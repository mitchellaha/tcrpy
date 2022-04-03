from tcr_interactions.post_models import GetUserSetting
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
    userSetting = GetUserSetting(settingName=settingName)
    response = requests.post(getUserSettingsURL, headers=headers, data=userSetting.json()).json()
    if response["d"] is str:
        responseLoad = json.loads(response["d"])
    else:
        responseLoad = response["d"]
    return responseLoad

def getGridSettings(gridID=None, gridName=None):
    """
    Gets The Grid Settings from TCR
        > GridID or GridName is required
    """
    if gridID is not None:
        gridSettingFormat = f"Yagna.Grid.{gridID}"
        gridSettings = getUserSettings(gridSettingFormat)
    elif gridName is not None:
        gridNumber = getGrid(gridName)["d"]["GridID"]
        gridSettingFormat = f"Yagna.Grid.{gridNumber}"
        gridSettings = getUserSettings(gridSettingFormat)
    return gridSettings

if __name__ == "__main__":
    # print(getUserSettings("Yagna.Grid.10"))
    # print(getGridSettings(gridID=1))
    print(getGridSettings(gridName="CJOBS"))
