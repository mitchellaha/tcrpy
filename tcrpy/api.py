import requests
import json
from tcrpy.models import *
from tcrpy.enums import *
from tcrpy.auth import auth

class GetGridData:
    def __init__(self, headers):
        self.headers = headers

class api:
    baseUrl = "http://apps.tcrsoftware.com/tcr_2"
    getGridDataURL = baseUrl + "/webservices/data.asmx/GetGridData"
    getTicketURL = baseUrl + "/webservices/Tickets.asmx/GetTicket"
    getJobURL = baseUrl + "/webservices/Jobs.asmx/GetJobByID"
    getCustomerURL = baseUrl + "/webservices/Customers.asmx/GetCustomer"
    getGridURL = baseUrl + "/webservices/config.asmx/GetGrid"
    getGridByIDURL = baseUrl + "/webservices/config.asmx/GetGridByID"
    getCompanyURL = baseUrl + "/webservices/GeneralAjaxService.asmx/GetCompany"
    getUserSettingsURL = baseUrl + "/webservices/UserSettings.asmx/GetUserSetting"
    getSideMenusURL = baseUrl + "/webservices/config.asmx/GetSideMenus"
    getGridColumnsForAdvSearchURL = baseUrl + "/webservices/config.asmx/GetGridColumnsForAdvSearch"
    getAuditDataURL = baseUrl + "/webservices/Audit.asmx/GetAuditData"
    getItemsURL = baseUrl + "/webservices/GeneralAjaxService.asmx/GetItems"

    def __init__(self, email=None, password=None):
        self.tcr_auth = auth(email, password)
        self.headers = self.tcr_auth.header
        self.sideMenu = None


    def getSideMenus(self):
        """Gets the Side Menus from TCR & Sets instance variable sideMenu"""
        request = requests.post(self.getSideMenusURL, headers=self.headers).json()
        self.sideMenus = request["d"]
        return request["d"]


    def manualGetGridData(self, PostDict, includeCount=False):
        """
        Gets the Grid Data from TCR  
            - PostDict is required
            - includeCount is optional

        Parameters
        ----------
            PostDict : dict
                The Dictionary Of Data To Post.
            includeCount : bool
                If True, Includes the Count of the returned Grid Data
        """
        response = requests.post(self.getGridDataURL, headers=self.headers, data=PostDict).json()
        resultjson = json.loads(response["d"]["Result"])
        count = resultjson["RecordCount"]
        data = resultjson["Data"]
        if includeCount:
            return {"count": count, "data": data}
        else:
            return data


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
            response = requests.post(self.getGridByIDURL, headers=self.headers, json={"gridID": grid}).json()
            return response["d"]
        if isinstance(grid, str):  # ? Uses "getGridURL" if grid is a str
            response = requests.post(self.getGridURL, headers=self.headers, json={"gridName": grid}).json()
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


    def getFilterFields(self, grid):
        """
        Gets The Default Filter Fields from TCR
            > GridID or GridName is required
        """
        getGrid = self.getGrid(grid)
        filterField = getGrid["FilterFields"].split(";")
        # defaultOperator = getGrid["DefaultSelect"]  # ? Not sure if this is the default operator or not...
        return filterField


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
        elif columns is not None:
            gridColumns = columns
        quickSearchFields = [field["DataField"] for field in gridColumns if field["QuickSearch"] is True]
        return quickSearchFields


    def getUserSettings(self, settingName):
        """
        Gets The User Settings from TCR
            > SettingName is required
        """
        response = requests.post(self.getUserSettingsURL, headers=self.headers, json={"settingName": settingName}).json()
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
        return self.getUserSettings(f"Yagna.Grid.{grid}")


    def getGridSortSettings(self, grid):
        """
        Gets the Grid Sort Settings if they Exist.
            > GridID or GridName is required
        """
        response = self.getGridSettings(grid)
        if response is not None and response["SortCol"]:
            return Sort(Attribute=response["SortCol"], Order=SortDir.fromSettings(response["SortDir"])).list()
        elif response is None:
            getGridInfo = self.getGrid(grid)
            if getGridInfo["DefaultSortColumn"] is not None:
                return Sort(Attribute=getGridInfo["DefaultSortColumn"], Order=SortDir.fromSettings(response["SortDir"])).list()
            else:
                return []


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


    def getGridData(self, Grid, FilterConditions=None,
                    StartIndex=1, RecordCount=250,
                    QuickSearch=None, IncludeCount=True,
                    ):
        """
        Gets The Grid Data from TCR

        Parameters::
        ----------
            Grid : str or int
            FilterConditions : dict
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

        if FilterConditions is None:
            FilterConditions = Filter()
        elif isinstance(FilterConditions, dict):
            FilterConditions = Filter(**FilterConditions)
        
        if QuickSearch is not None:
            quickSearchFields = [field["DataField"] for field in getGridInfo["Columns"] if field["QuickSearch"] is True]
            FilterConditions.add_advanced_filter(Filter().add_quick_search_filter(QuickSearch, quickSearchFields))

        if isinstance(FilterConditions, Filter):
            FilterConditions = FilterConditions.dict()
            pass

        requestData = GetGridDateRootModel(
            query=GetGridDataModel(
                GridID=getGridInfo["GridID"],
                RecordCount=RecordCount,
                Filter=FilterConditions,
                StartIndex=StartIndex,
                Attributes=attributeFields,
                Sort=self.getGridSortSettings(gridID),
                CustomSort=None,
            )
        ).json()

        response = requests.post(self.getGridDataURL, headers=self.headers, data=requestData).json()
        resultjson = json.loads(response["d"]["Result"])
        if IncludeCount is True:
            return {"count": resultjson["RecordCount"], "data": resultjson["Data"]}
        else:
            return resultjson["Data"]

    def getTicket(self, ticketID: int):
        """
        Gets the Ticket Details from TCR

        Parameters::
        ----------
            ticketID -- Ticket ID : int

        Returns::
        -------
            dict -- Ticket Details
        """
        ticketID = {"ticketID": ticketID}
        response = requests.post(self.getTicketURL, headers=self.headers, json=ticketID).json()
        return response["d"]

    def getJob(self, jobID: int):
        """
        Gets the Job Details from TCR

        Parameters::
        ----------
            jobID -- Job ID : int

        Returns::
        -------
            dict -- Job Details
        """
        jobID = {"JobID": jobID}
        response = requests.post(self.getJobURL, headers=self.headers, json=jobID).json()
        return response["d"]

    def getCustomer(self, custID: int):
        """
        Gets the Customer Details from TCR

        Parameters::
        ----------
            custID -- Customer ID : int

        Returns::
        -------
            dict -- Customer Details
        """
        custID = {"custID": custID}
        response = requests.post(self.getCustomerURL, headers=self.headers, json=custID).json()
        return response["d"]

    def getItems(self):
        """
        Gets all the Items from TCR

        Returns::
        -------
            dict -- Items
        """
        response = requests.post(self.getItemsURL, headers=self.headers).json()
        return response["d"]

    def getCompany(self):
        """
        Gets Your Company Details from TCR

        Returns::
        -------
            dict -- Company Details
        """
        response = requests.post(self.getCompanyURL, headers=self.headers).json()
        dResponse = response["d"]
        dResponse.pop("LogoImage")
        return dResponse