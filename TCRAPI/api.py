import requests
import json
from TCRAPI.models import *
from TCRAPI.enums import *
from TCRAPI.utils import getGridDataQuickSearch

class api:
    baseUrl = "http://apps.tcrsoftware.com/tcr_2/"
    getCompanyURL = baseUrl + "webservices/GeneralAjaxService.asmx/GetCompany"
    getGridURL = baseUrl + "webservices/config.asmx/GetGrid"
    getGridByIDURL = baseUrl + "webservices/config.asmx/GetGridByID"
    getGridDataURL = baseUrl + "webservices/data.asmx/GetGridData"
    getUserSettingsURL = baseUrl + "webservices/UserSettings.asmx/GetUserSetting"
    getSideMenusURL = baseUrl + "webservices/config.asmx/GetSideMenus"
    getGridColumnsForAdvSearchURL = baseUrl + "webservices/config.asmx/GetGridColumnsForAdvSearch"
    getAuditDataURL = baseUrl + "webservices/Audit.asmx/GetAuditData"
    getTicketURL = baseUrl + "webservices/Tickets.asmx/GetTicket"
    getJobURL = baseUrl + "webservices/Jobs.asmx/GetJobByID"
    getCustomerURL = baseUrl + "webservices/Customers.asmx/GetCustomer"
    getItemsURL = baseUrl + "webservices/GeneralAjaxService.asmx/GetItems"

    def __init__(self, headers=None):
        self.headers = headers
        self.sideMenu = None


    def getGrid(self, grid):
        """
        Gets The Full JSON Response from TCR with Grid Name  
            - Uses GetGridByID url if grid is an int
            - Uses GetGrid url if grid is a string
        
        Parameters:
        ----------
            grid : str

        Returns:
        -------
            dict : contains the grid info
        """
        if isinstance(grid, int):  # ? Uses "getGridByIDURL" if grid is an int
            grid = GetGridByIDModel(gridID=grid)
            response = requests.post(self.getGridByIDURL, headers=self.headers, data=grid.json()).json()
            return response["d"]
        if isinstance(grid, str):  # ? Uses "getGridURL" if grid is a str
            grid = GetGridModel(gridName=grid)
            response = requests.post(self.getGridURL, headers=self.headers, data=grid.json()).json()
            return response["d"]
        else:
            raise ValueError("Grid must be a string or int")


    def gridNameID(self, grid):
        """
        If Given the GridName, Returns the GridID
        If Given the GridID, Returns the GridName
        """
        gridInfo = self.getGrid(grid)
        if isinstance(grid, str):
            return gridInfo["GridID"]
        if isinstance(grid, int):
            return gridInfo["GridName"]


    def getGridDataFields(self, grid=None, columns=None):
        """
        Gets The Required Field Attributes from the Grid Name

        Parameters::
        ----------
            grid -- grid name or grid id : str or int
            columns -- list of columns to search : list of dict


        Returns::
        -------
            list[str] | Data Fields
        """
        if grid is not None:
            grid = self.getGrid(grid)
        if columns is not None:
            grid = columns
        else:
            raise ValueError("Grid or Columns are required to get the Data Fields")
        return [field["DataField"] for field in grid["Columns"]]


    def getGridQuickSearchFields(self, grid=None, columns=None):
        """
        Gets The QuickSearch Fields either grid or columns  

        Parameters::
        ----------
            grid -- grid name or grid id : str or int  
            columns -- list of columns to search : list of dict

        Returns::
        -------
            list[str] | Quick Search Fields
        """
        if grid is not None:
            gridColumns = self.getGrid(grid)["Columns"]
        if columns is not None:
            gridColumns = columns
        quickSearchFields = [field["DataField"] for field in gridColumns if field["QuickSearch"] is True]
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
            return json.loads(response["d"])
        else:
            return response["d"]


    def getGridSettings(self, grid):
        """
        Gets The Grid Settings from TCR
            > GridID or GridName is required
        """
        if isinstance(grid, str):
            grid = self.gridNameID(grid)
        gridSettingFormat = f"Yagna.Grid.{grid}"
        gridSettings = self.getUserSettings(gridSettingFormat)
        return gridSettings


    def getGridSortSettings(self, grid):
        """
        Gets the Grid Sort Settings if they Exist.
            > GridID or GridName is required
        """
        response = self.getGridSettings(grid)
        if response is not None and response["SortCol"]:
            return SortModel(Attribute=response["SortCol"], Order=SortDir.fromSettings(response["SortDir"]))
        if response is None:
            getGridInfo = self.getGrid(grid)
            if getGridInfo["DefaultSortColumn"] is not None:
                return SortModel(Attribute=getGridInfo["DefaultSortColumn"], Order=getGridInfo["DefaultSortOrder"])
            else:
                return SortModel()


    def getSideMenus(self):
        """Gets the Side Menus from TCR & Sets instance variable sideMenu"""
        request = requests.post(self.getSideMenusURL, headers=self.headers).json()
        self.sideMenus = request["d"]
        return request["d"]


    def getColumnsForAdvSearch(self, grid):
        """
        Gets the Columns for Advanced Search from TCR
        
        Parameters::
        ----------
            grid -- grid name or grid id : str or int

        Returns::
        -------
            list[dict] | List of Dictionaries Containing Column Info
        """
        gridName = self.getGrid(grid)["GridName"]
        payload = {"gridName": gridName}
        response = requests.post(self.getGridColumnsForAdvSearchURL, headers=self.headers, json=payload).json()
        return response["d"]


    def getGridData(self, Grid, FilterConditions,
                    StartIndex=1, RecordCount=250,
                    QuickSearch=None, IncludeCount=True,
                    ):
        """
        Gets The Grid Data from TCR

        Parameters::
        ----------
            Grid : str or int
            FilterConditions : list
            StartIndex : int (default=1)
            RecordCount : int (default=250)
            QuickSearch : str (default=None)
            IncludeCount : bool (default=True)

        Returns::
        -------
            dict : contains the grid data and count
        """
        getGridInfo = self.getGrid(Grid)
        gridID = getGridInfo["GridID"]
        attributeFields = [field["DataField"] for field in getGridInfo["Columns"] ]
        
        if QuickSearch is not None:
            quickSearchFields = [field["DataField"] for field in getGridInfo["Columns"] if field["QuickSearch"] is True]
            FilterConditions = getGridDataQuickSearch(
                SearchQuery=QuickSearch,
                GridFilterConditions=FilterConditions.Conditions,
                QuickSearchFieldsList=quickSearchFields
            )

        requestData = GetGridDataModelRoot(
            query=GetGridDataModel(
                GridID=getGridInfo["GridID"],
                RecordCount=RecordCount,
                Filter=FilterConditions,
                StartIndex=StartIndex,
                Attributes=attributeFields,
                Sort=[self.getGridSortSettings(gridID)],
                CustomSort=None,
            )
        ).json()

        response = requests.post(self.getGridDataURL, headers=self.headers, data=requestData).json()
        resultjson = json.loads(response["d"]["Result"])
        count = resultjson["RecordCount"]
        data = resultjson["Data"]
        if IncludeCount is True:
            return {"count": count, "data": data}
        else:
            return data

    def getTicket(self, ticketID):
        """
        Gets the Ticket Details from TCR

        Parameters::
        ----------
            ticketID -- Ticket ID : int

        Returns::
        -------
            dict -- Ticket Details
        """
        ticketID = getTicketModel(ticketID=ticketID).json()
        response = requests.post(self.getTicketURL, headers=self.headers, data=ticketID).json()
        return response["d"]

    def getCompany(self):
        """
        Gets the Company Details from TCR

        Returns::
        -------
            dict -- Company Details
        """
        response = requests.post(self.getCompanyURL, headers=self.headers).json()
        dResponse = response["d"]
        dResponse.pop("LogoImage")
        return dResponse

    def getJob(self, jobID):
        """
        Gets the Job Details from TCR

        Parameters::
        ----------
            jobID -- Job ID : int

        Returns::
        -------
            dict -- Job Details
        """
        jobID = getJobModel(JobID=jobID).json()
        response = requests.post(self.getJobURL, headers=self.headers, data=jobID).json()
        return response["d"]

    def getCustomer(self, custID):
        """
        Gets the Customer Details from TCR

        Parameters::
        ----------
            custID -- Customer ID : int

        Returns::
        -------
            dict -- Customer Details
        """
        custID = getCustomerModel(custID=custID).json()
        response = requests.post(self.getCustomerURL, headers=self.headers, data=custID).json()
        return response["d"]

    def getItems(self):
        """
        Gets the Items from TCR

        Returns::
        -------
            dict -- Items
        """
        response = requests.post(self.getItemsURL, headers=self.headers).json()
        return response["d"]