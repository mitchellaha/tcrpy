from tcr_interactions.tcr_auth import tcrAuth
from tcr_interactions.post_models import GetGridByIDModel, GetGridModel, GetUserSettingModel, SortModel, GetGridDataModel, GetGridDataModelRoot
from dotenv import load_dotenv
import json
import os
import requests

class TCRAPI:
    def __init__(self, email=None, password=None):
        load_dotenv()
        self.email = email
        if email is None:
            self.email = os.getenv("email")

        self.password = password
        if password is None:
            self.password = os.getenv("password")

        self.auth = tcrAuth(email=self.email, password=self.password)
        self.headers = self.getHeaders()
        self.baseUrl = "http://apps.tcrsoftware.com/tcr_2"
        self.getGridURL = self.baseUrl + "/webservices/config.asmx/GetGrid"
        self.getGridByIDURL = self.baseUrl + "/webservices/config.asmx/GetGridByID"
        self.getGridDataURL = self.baseUrl + "/webservices/data.asmx/GetGridData"
        self.getUserSettingsURL = self.baseUrl + "/webservices/config.asmx/GetUserSettings"


    def getHeaders(self):
        tcr = self.auth
        tcr.login()
        self.headers = tcr.headers
        return tcr.headers


    def getGrid(self, gridName):
        """
        Gets The Full JSON Response from TCR with Grid Name
            > GridName is required
        """
        if isinstance(gridName, int):
            gridName = self.gridNameID(gridName)
        grid = GetGridModel(gridName=gridName)
        response = requests.post(self.getGridURL, headers=self.headers, data=grid.json()).json()
        data = response["d"]
        return data

    def getGridByID(self, gridID):
        """
        Gets The Full JSON Response from TCR with Grid ID
            > GridID is required
        """
        if isinstance(gridID, str):
            gridID = self.gridNameID(gridID)
        grid = GetGridByIDModel(gridID=gridID)
        response = requests.post(self.getGridByIDURL, headers=self.headers, data=grid.json()).json()
        data = response["d"]
        return data

    def gridNameID(self, grid):
        """
        If Given the GridName, Returns the GridID
        If Given the GridID, Returns the GridName
        """
        if isinstance(grid, str):
            grid = self.getGrid(grid)
            gridReturn = grid["GridID"]
        if isinstance(grid, int):
            grid = self.getGridByID(grid)
            gridReturn = grid["GridName"]
        return gridReturn

    def getGridInfo(self, grid):
        """
        Gets The Relevant GridInfo from GridName
            > GridName is required
        """
        gridInfo = {}
        grid = self.getGrid(grid)
        gridInfo["GridTitle"] = grid["GridTitle"]
        gridInfo["GridName"] = grid["GridName"]
        gridInfo["GridID"] = grid["GridID"]
        gridInfo["PrimaryKeyField"] = grid["PrimaryKeyField"]
        gridInfo["EditURL"] = grid["EditURL"]
        gridInfo["FilterFields"] = grid["FilterFields"]
        gridInfo["Columns"] = grid["Columns"]
        return gridInfo


    def getGridDataFields(self, grid):
        """
        Gets The Required Field Attributes from the Grid Name
            > GridName is required
        """
        gridData = self.getGrid(grid)
        dataFields = []
        for dField in gridData["Columns"]:
            dataFields.append(dField["DataField"])
        return dataFields

    def getGridDataFieldsInfo(self, grid):
        """
        Gets The Fields with all info from the Grid Name
            > GridName is required
        """
        gridData = self.getGrid(grid)
        dataFields = []
        for dField in gridData["Columns"]:
            dataFields.append(dField)
        return dataFields

    def getGridQuickSearchFields(self, grid):
        """
        Gets The QuickSearch Fields from the Grid Name
            > GridName is required
        """
        gridFields = self.getGridDataFieldsInfo(grid)
        quickSearchFields = []
        for field in gridFields:
            if field["QuickSearch"] is True:
                quickSearchFields.append(field["DataField"])
        return quickSearchFields


    def getUserSettings(self, settingName):
        """
        Gets The User Settings from TCR
            > SettingName is required
        """
        userSetting = GetUserSettingModel(settingName=settingName)
        response = requests.post(
            self.getUserSettingsURL, headers=self.headers, data=userSetting.json()).json()
        if isinstance(response["d"], str):
            responseLoad = json.loads(response["d"])
        else:
            responseLoad = response["d"]
        return responseLoad


    def getGridSettings(self, grid):
        """
        Gets The Grid Settings from TCR
            > GridID or GridName is required
        """
        if isinstance(grid, str):
            gridNumber = self.getGrid(grid)["d"]["GridID"]
            gridSettingFormat = f"Yagna.Grid.{gridNumber}"
            gridSettings = self.getUserSettings(gridSettingFormat)
        if isinstance(grid, int):
            gridSettingFormat = f"Yagna.Grid.{grid}"
            gridSettings = self.getUserSettings(gridSettingFormat)
        return gridSettings


    def getGridSortSettings(self, grid):
        """
        Gets the Grid Sort Settings if they Exist.
            > GridID or GridName is required
        """
        response = self.getGridSettings(grid)
        if response is not None:
            if response["SortDir"] == "sort-asc":
                sortDirINT = 0
            if response["SortDir"] == "sort-desc":
                sortDirINT = 1
            sort = SortModel(
                Attribute=response["SortCol"],
                Order=sortDirINT
            )
            return sort
        else:  # ? If there is no sort settings find the default sort settings
            getGridInfo = self.getGrid(grid)
            if getGridInfo is not None and getGridInfo["DefaultSortColumn"] is not None:
                sort = SortModel(
                    Attribute=getGridInfo["DefaultSortColumn"],
                    Order=getGridInfo["DefaultSortOrder"])
                return sort
            else:
                sort = SortModel()
                return sort


    def getGridData(self, Grid, FilterConditions, StartIndex=1, RecordCount=250):
        getGridInfo = self.getGrid(Grid)
        gridID = getGridInfo["GridID"]

        requestData = GetGridDataModelRoot(
            query=GetGridDataModel(
                GridID=gridID,
                RecordCount=RecordCount,
                Filter=FilterConditions,
                StartIndex=StartIndex,
                Attributes=self.getGridDataFields(gridID),
                Sort=[self.getGridSortSettings(gridID)],
                CustomSort=None,
            )
        ).json()
        response = requests.post(
            self.getGridDataURL, headers=self.headers, data=requestData).json()
        resultjson = json.loads(response["d"]["Result"])
        count = resultjson["RecordCount"]
        data = resultjson["Data"]
        return count, data
