import requests
import json
from tcrpy.models import *
from tcrpy.enums import *
from tcrpy.auth import auth
import datetime as dt
from tcrpy.utils import millisecond_stamp_to_datetime

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
    getGridColumnsURL = baseUrl + "/webservices/Config.asmx/GetGridColumns"
    getAuditDataURL = baseUrl + "/webservices/Audit.asmx/GetAuditData"
    getItemsURL = baseUrl + "/webservices/GeneralAjaxService.asmx/GetItems"
    getPriceListsURL = baseUrl + "/webservices/PriceListService.asmx/GetPriceLists"
    getInvoiceItemPriceURL = baseUrl + "/webservices/GeneralAjaxService.asmx/GetInvoiceItemPrice"
    getPriceListItemURL = baseUrl + "/webservices/GeneralAjaxService.asmx/GetPriceListItem"
    getNewItemForQuoteURL = baseUrl + "/webservices/QuoteService.asmx/GetNewItemForQuote"
    getDriversURL = baseUrl + "/webservices/Drivers.asmx/GetAllDrivers"
    getEquipmentURL = baseUrl + "/webservices/GeneralAjaxService.asmx/GetEquipment"
    getEmployeesURL = baseUrl + "/webservices/Employees.asmx/GetDrivers"
    getSubItemsURL = baseUrl + "/webservices/GeneralAjaxService.asmx/GetSubItems"

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

    def getGridColumns(self, grid):
        """
        Gets the Grid Columns from TCR
        """
        if isinstance(grid, str):
            grid = self.gridNameID(grid)
        response = requests.post(self.getGridColumnsURL, headers=self.headers, json={"gridID": grid}).json()
        return response["d"]


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
        if response is None:
            getGridInfo = self.getGrid(grid)
            if getGridInfo["DefaultSortColumn"] is not None:
                return Sort(Attribute=getGridInfo["DefaultSortColumn"], Order=getGridInfo["DefaultSortOrder"]).list()
            else:
                return []
        if response["SortCol"]:
            return Sort(Attribute=response["SortCol"], Order=SortDir.fromSettings(response["SortDir"])).list()
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
        attributeFields = [field["DataField"] for field in getGridInfo["Columns"]]
        dateField = [field["DataField"] for field in getGridInfo["Columns"] if field["DataType"] == 4]

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
        for field in dateField:
            for row in resultjson["Data"]:
                if row[field] is not None:
                    splitDot = row[field].split(".")
                    row[field] = dt.datetime.strptime(splitDot[0], "%Y-%m-%dT%H:%M:%S")
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
        responseD = response["d"]
        dateKeys = ["TicketDate", "DelPUDate", "DateCreated", "DateUpdated", "PortalDateCreated",
                    "VoidDate", "DateSigned", "DateSigned_Adjusted", "DriverCompletedDate",
                    "DateFinalEdited", "EstimatedStartTime", "EstimatedEndTime"]
        for key in dateKeys:
            if responseD[key] is not None:
                responseD[key] = millisecond_stamp_to_datetime(responseD[key])
            if responseD["OriginalRecordData"][key] is not None:
                responseD["OriginalRecordData"][key] = millisecond_stamp_to_datetime(responseD["OriginalRecordData"][key])
        return responseD


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
        responseD = response["d"]
        dateKeys = [
            "DateOpened", "PermitExpiration", "CloseDate", "EstCloseDate", "ContractStart",
            "ContractExpiration", "FirstBillingDate", "LastBillingDate", "DateCreated",
            "DateUpdated", "PortalDateCreated", "PreliminaryNoticeSent", "PreliminaryNoticeReturn",
            "EstStartDate", "FirstTicket", "LastTicket", "LastInvoiceDate"
        ]
        for key in dateKeys:
            if responseD[key] is not None:
                responseD[key] = millisecond_stamp_to_datetime(responseD[key])
            if responseD["OriginalRecordData"][key] is not None:
                responseD["OriginalRecordData"][key] = millisecond_stamp_to_datetime(responseD["OriginalRecordData"][key])
        return responseD


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
        dateKeys = ["DateOpened", "DateCreated", "DateUpdated", "InsurCertExpiration"]
        responseD = response["d"]
        for key in dateKeys:
            if responseD[key] is not None:
                responseD[key] = millisecond_stamp_to_datetime(responseD[key])
            if responseD["OriginalRecordData"][key] is not None:
                responseD["OriginalRecordData"][key] = millisecond_stamp_to_datetime(responseD["OriginalRecordData"][key])
        return responseD


    def getItems(self):
        """
        Gets all the Items from TCR

        Returns::
        -------
            dict -- Items
        """
        response = requests.post(self.getItemsURL, headers=self.headers).json()
        dateKeys = ["DateCreated", "DateUpdated", "LastOrderDate"]
        responseD = response["d"]
        for item in responseD:
            for key in dateKeys:
                if item[key] is not None:
                    item[key] = millisecond_stamp_to_datetime(item[key])
                if item["OriginalRecordData"] is not None:
                    if item["OriginalRecordData"][key] is not None:
                        item["OriginalRecordData"][key] = millisecond_stamp_to_datetime(item["OriginalRecordData"][key])
        return responseD

    def getPriceLists(self):
        """
        Gets all the Price Lists from TCR

        Returns::
        -------
            dict -- Price Lists
        """
        dateKeys = ["DateCreated", "DateUpdated"]
        response = requests.post(self.getPriceListsURL, headers=self.headers).json()
        for item in response["d"]:
            for key in dateKeys:
                if item[key] is not None:
                    item[key] = millisecond_stamp_to_datetime(item[key])
        return response["d"]

    def getPriceListItem(self, itemID: int, priceID: int):
        """
        Gets the Price List Item Details from TCR

        Parameters::
        ----------
            itemID -- Item ID : int
            priceID -- Price List ID : int

        Returns::
        -------
            dict -- Price List Item Details
        """
        priceListItem = {"itemID": itemID, "priceID": priceID}
        response = requests.post(self.getPriceListItemURL, headers=self.headers, json=priceListItem).json()
        dateKeys = ["DateCreated", "DateUpdated"]
        responseD = response["d"]
        for key in dateKeys:
            if responseD[key] is not None:
                responseD[key] = millisecond_stamp_to_datetime(responseD[key])
        return responseD

    def getInvoiceItemPrice(self, invoiceID, jobID, itemID):
        """
        Gets the Invoice Item Price from TCR

        Parameters::
        ----------
            invoiceID -- Invoice ID : int
            jobID -- Job ID : int
            itemID -- Item ID : int

        Returns::
        -------
            dict -- Invoice Item Price
        """
        dateKeys = ["DateCreated", "DateUpdated"]
        postData = {"invoiceID": invoiceID, "jobID": jobID, "itemID": itemID}
        response = requests.post(self.getInvoiceItemPriceURL, headers=self.headers, json=postData).json()
        for key in dateKeys:
            if response["d"][key] is not None:
                response["d"][key] = millisecond_stamp_to_datetime(response["d"][key])
        return response["d"]

    def getNewItemForQuote(self, quoteID, itemID):
        """
        Gets the New Item for Quote from TCR

        Parameters::
        ----------
            quoteID -- Quote ID : int
            itemID -- Item ID : int

        Returns::
        -------
            dict -- New Item for Quote
        """
        dateKeys = ["DateCreated", "DateUpdated"]
        postData = {"quoteID": quoteID, "itemID": itemID}
        response = requests.post(self.getNewItemForQuoteURL, headers=self.headers, json=postData).json()
        for key in dateKeys:
            if response["d"][key] is not None:
                response["d"][key] = millisecond_stamp_to_datetime(response["d"][key])
        return response["d"]

    def getCompany(self):
        """
        Gets Your Company Details from TCR

        Returns::
        -------
            dict -- Company Details
        """
        response = requests.post(self.getCompanyURL, headers=self.headers).json()
        responseD = response["d"]
        responseD.pop("LogoImage")
        return responseD

    def getDrivers(self):
        """
        Gets All Drivers From TCR
        
        Returns::
        -------
            list - All Drivers
        """
        response = requests.post(self.getDriversURL, headers=self.headers).json()
        dateKeys = ["LocationDate", "DateCreated", "DateUpdated"]
        responseD = response["d"]
        for driver in responseD:
            for key in dateKeys:
                if driver[key] is not None:
                    driver[key] = millisecond_stamp_to_datetime(driver[key])
                if driver["OriginalRecordData"] is not None:
                    if driver["OriginalRecordData"][key] is not None:
                        driver["OriginalRecordData"][key] = millisecond_stamp_to_datetime(driver["OriginalRecordData"][key])
        return responseD

    def getEmployees(self):
        """
        Gets All Employees From TCR
        
        Returns::
        -------
            list - All Employees
        """
        response = requests.post(self.getEmployeesURL, headers=self.headers).json()
        dateKeys = ["DateCreated", "DateUpdated"]
        responseD = response["d"]
        for employee in responseD:
            for key in dateKeys:
                if employee[key] is not None:
                    employee[key] = millisecond_stamp_to_datetime(employee[key])
                if employee["OriginalRecordData"] is not None:
                    if employee["OriginalRecordData"][key] is not None:
                        employee["OriginalRecordData"][key] = millisecond_stamp_to_datetime(employee["OriginalRecordData"][key])
        return responseD

    def getEquipment(self, EquipmentID):
        """
        Gets All Equipment From TCR

        Parameters::
        ----------
            EquipmentID -- Equipment ID : int
        
        Returns::
        -------
            list - All Equipment
        """
        requestData = {"equipID": EquipmentID}
        response = requests.post(self.getEquipmentURL, headers=self.headers, json=requestData).json()
        dateKeys = ["DateCreated", "DateInService", "DateUpdated", "DateOutofService"]
        responseD = response["d"]
        for key in dateKeys:
            if responseD[key] is not None:
                responseD[key] = millisecond_stamp_to_datetime(responseD[key])
            if responseD["OriginalRecordData"][key] is not None:
                responseD["OriginalRecordData"][key] = millisecond_stamp_to_datetime(responseD["OriginalRecordData"][key])
        return responseD

    def getSubItems(self):
        """
        Gets All Sub Items From TCR
        
        Returns::
        -------
            list - All Sub Items
        """
        response = requests.post(self.getSubItemsURL, headers=self.headers).json()
        dateKeys = ["DateCreated", "DateUpdated"]
        responseD = response["d"]
        for key in dateKeys:
            if responseD[key] is not None:
                responseD[key] = millisecond_stamp_to_datetime(responseD[key])
            if responseD["OriginalRecordData"][key] is not None:
                responseD["OriginalRecordData"][key] = millisecond_stamp_to_datetime(responseD["OriginalRecordData"][key])
        return responseD
