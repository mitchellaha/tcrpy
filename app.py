from typing import List, Optional, Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from TCRAPI.api import api
from TCRAPI.auth import auth
from TCRAPI.getgriddata import *


tcrAuth = auth()
tcr = api(
    headers=tcrAuth.header,
)

app = FastAPI(
    title="TCR-API",
    description="For serving TCR data as a REST API",
)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Directory and Functions of API as a Dictionary to be Served to Root
definitions = {
    "Purpose": "Each Endpoint Shown Below is a Function of the API with the data needed",
    "get_Grid": {
        "type": "post",
        "url": "/getgrid/",
        "parameters": {
            "grid": "int"
        },
    },
    "get_grid_settings": {
        "type": "post",
        "url": "/getgridsettings/",
        "parameters": {
            "grid": "int"
        },
    },
    "get_side_menus": {
        "type": "post",
        'url': "/getsidemenus/",
        "parameters": None
    },
    "schedule": {
        "type": "post",
        "url": "/schedule/",
        "parameters": {
            "start": "MM/DD/YYYY",
            "end": "MM/DD/YYYY",
            "include_count": False
        },
    },
    "ticket_items": {
        "type": "post",
        "url": "/titems/",
        "parameters": {
            "ticketid": "int",
            "include_count": False
        },
    },
    "customer_jobs": {
        "type": "post",
        "url": "/cjobs/",
        "parameters": {
            "customerid": "int",
            "include_count": False
        },
    },
    "customer_invoices": {
        "type": "post",
        "url": "/cinvoices/",
        "parameters": {
            "customerid": "int",
            "include_count": False
        },
    },
    "invoice_details": {
        "type": "post",
        "url": "/idetails/",
        "parameters": {
            "invoiceid": "int",
            "include_count": False
        },
    },
    "customer_contacts": {
        "type": "post",
        "url": "/ccontacts/",
        "parameters": {
            "customerid": "int",
            "include_count": False
        },
    },
    "customers": {
        "type": "post",
        "url": "/customers/",
        "parameters": {
            "search": "str",
            "status": "str",
            "include_count": False
        },
    },
    "jobs": {
        "type": "post",
        "url": "/jobs/",
        "parameters": {
            "search": "str",
            "status": "str",
            "include_count": False
        },
    },
    "job_tickets": {
        "type": "post",
        "url": "/jtickets/",
        "parameters": {
            "jobid": "int",
            "include_count": False
        },
    },
    "job_invoices": {
        "type": "post",
        "url": "/jinvoices/",
        "parameters": {
            "jobid": "int",
            "include_count": False
        },
    },
    "ticket_labor": {
        "type": "post",
        "url": "/tlabor/",
        "parameters": {
            "ticketid": "int",
            "include_count": False
        },
    },
    "labour_tickets": {
        "type": "post",
        "url": "/ltickets/",
        "parameters": {  # TODO: Maybe Add a Search by Date & Certified?
            "include_count": False
        },
    },
    "ticket_signs": {
        "type": "post",
        "url": "/tsigns/",
        "parameters": {
            "ticketid": "int",
            "include_count": False
        },
    },
    "ticket_return_signs": {
        "type": "post",
        "url": "/trsigns/",
        "parameters": {
            "ticketid": "int",
            "include_count": False
        },
    },
    "line_items": {
        "type": "post",
        "url": "/lineitems/",
        "parameters": {
            "search": "str",
            "include_count": False
        },
    },
    "drivers": {
        "type": "post",
        "url": "/drivers/",
        "parameters": {
            "search": "str",
            "include_count": False
        },
    },
    "invoices": {
        "type": "post",
        "url": "/invoices/",
        "parameters": {
            "search": "str",
            "include_count": False
        },
    },
    "price_list_items": {
        "type": "post",
        "url": "/plitems/",
        "parameters": {
            "PriceListID": "int",
            "search": "str",
            "include_count": False
        },
    },
    "price_lists": {
        "type": "post",
        "url": "/plists/",
        "parameters": {
            "search": "str",
            "include_count": False
        },
    },
}


class GetGrid(BaseModel):
    grid: int

class GetGridSettings(BaseModel):
    grid: int

class GetSideMenus(BaseModel):
    pass

class GetGridBaseModel(BaseModel):
    search: Optional[str]
    include_count: Optional[bool] = True
    start_index: Optional[int] = 1
    record_count: Optional[int] = 250

class Schedule(GetGridBaseModel):
    start: str
    end: str

class TicketItems(GetGridBaseModel):
    ticketid: int

class CustomerJobs(GetGridBaseModel):
    customerid: int

class CustomerInvoices(GetGridBaseModel):
    customerid: int

class InvoiceDetails(GetGridBaseModel):
    invoiceid: int

class CustomerContacts(GetGridBaseModel):
    customerid: int

class Customers(GetGridBaseModel):
    status: Optional[Union[str, List[str]]]

class Jobs(GetGridBaseModel):
    status: Optional[Union[str, List[str]]]

class JobTickets(GetGridBaseModel):
    jobid: int

class JobInvoices(GetGridBaseModel):
    jobid: int

class TicketLabor(GetGridBaseModel):
    ticketid: int

class LaborTickets(GetGridBaseModel):
    pass

class TicketSigns(GetGridBaseModel):
    ticketid: int

class TicketReturnSigns(GetGridBaseModel):
    ticketid: int

class LineItems(GetGridBaseModel):
    pass

class Drivers(GetGridBaseModel):
    pass

class Invoices(GetGridBaseModel):
    pass

class PriceListItems(GetGridBaseModel):
    pricelistid: int

class PriceLists(GetGridBaseModel):
    pass


# ! Basic Info Function
@ app.get("/")
def read_root():
    return definitions


# ! Basic Info Function
@ app.post("/getgrid/")  # ? Returns the Full GetGrid Post of TCR
async def get_gridpost(grid: GetGrid):
    response = tcr.getGrid(grid.grid)
    return response


# ! Basic Info Function
@ app.post("/getgridsettings/")  # ? Returns the Full GetGridSettings Post of TCR
async def get_gridsettingspost(grid: GetGridSettings):
    response = tcr.getGridSettings(grid.grid)
    return response


# ! Basic Info Function
@ app.post("/getsidemenus/")  # ? Returns the Full GetSideMenus Post of TCR
async def get_sidemenuspost():
    response = tcr.getSideMenus()
    return response



@ app.post("/customers/")
async def get_customers(customers: Customers):
    info = customersClass()
    
    if customers.status:
        info.setStatusFilter(customers.status)

    request = tcr.getGridData(
        Grid=info.gridID,
        FilterConditions=info.filterConditions,
        QuickSearch=customers.search,
        StartIndex=customers.start_index,
        RecordCount=customers.record_count,
        IncludeCount=customers.include_count)
    return request


@ app.post("/jobs/")
async def get_jobs(jobs: Jobs):
    info = jobsClass()
    
    if jobs.status:
        info.setStatusFilter(jobs.status)

    request = tcr.getGridData(
        Grid=info.gridID,
        FilterConditions=info.filterConditions,
        QuickSearch=jobs.search,
        StartIndex=jobs.start_index,
        RecordCount=jobs.record_count,
        IncludeCount=jobs.include_count)
    return request


@ app.post("/invoices/")
async def get_invoices(invoices: Invoices):
    info = invoicesClass()

    request = tcr.getGridData(  # TODO: Make These Get Grid Data Functions Repeat Less
        Grid=info.gridID,
        FilterConditions=info.filterConditions,
        QuickSearch=invoices.search,
        StartIndex=invoices.start_index,
        RecordCount=invoices.record_count,
        IncludeCount=invoices.include_count)
    return request


@ app.post("/schedule/")
async def get_schedule(schedule: Schedule):
    info = driverScheduleClass(schedule.start, schedule.end)

    request = tcr.getGridData(
        Grid=info.gridID,
        FilterConditions=info.filterConditions,
        QuickSearch=schedule.search,
        StartIndex=schedule.start_index,
        RecordCount=schedule.record_count,
        IncludeCount=schedule.include_count)
    return request


@ app.post("/titems/")  # ? Returns the Items for the Provided Ticket
async def get_items(items: TicketItems):
    info = ticketItemsClass(items.ticketid)

    request = tcr.getGridData(
        Grid=info.gridID,
        FilterConditions=info.filterConditions,
        QuickSearch=items.search,
        StartIndex=items.start_index,
        RecordCount=items.record_count,
        IncludeCount=items.include_count)
    return request



@ app.post("/cjobs/")
async def get_cjobs(cjobs: CustomerJobs):
    info = customerJobsClass(cjobs.customerid)

    request = tcr.getGridData(
        Grid=info.gridID,
        FilterConditions=info.filterConditions,
        QuickSearch=cjobs.search,
        StartIndex=cjobs.start_index,
        RecordCount=cjobs.record_count,
        IncludeCount=cjobs.include_count)
    return request


@ app.post("/cinvoices/")
async def get_cinvoices(cinvoices: CustomerInvoices):
    info = customerInvoicesClass(cinvoices.customerid)

    request = tcr.getGridData(
        Grid=info.gridID,
        FilterConditions=info.filterConditions,
        QuickSearch=cinvoices.search,
        StartIndex=cinvoices.start_index,
        RecordCount=cinvoices.record_count,
        IncludeCount=cinvoices.include_count)
    return request


@ app.post("/idetails/")
async def get_idetails(idetails: InvoiceDetails):
    info = invoiceDetailsClass(idetails.invoiceid)

    request = tcr.getGridData(
        Grid=info.gridID,
        FilterConditions=info.filterConditions,
        QuickSearch=idetails.search,
        StartIndex=idetails.start_index,
        RecordCount=idetails.record_count,
        IncludeCount=idetails.include_count)
    return request


@ app.post("/ccontacts/")
async def get_ccontacts(ccontacts: CustomerContacts):
    info = customerContactsClass(ccontacts.customerid)

    request = tcr.getGridData(
        Grid=info.gridID,
        FilterConditions=info.filterConditions,
        QuickSearch=ccontacts.search,
        StartIndex=ccontacts.start_index,
        RecordCount=ccontacts.record_count,
        IncludeCount=ccontacts.include_count)
    return request


@ app.post("/jtickets/")
async def get_jtickets(jtickets: JobTickets):
    info = jobTicketsClass(jtickets.jobid)

    request = tcr.getGridData(
        Grid=info.gridID,
        FilterConditions=info.filterConditions,
        QuickSearch=jtickets.search,
        StartIndex=jtickets.start_index,
        RecordCount=jtickets.record_count,
        IncludeCount=jtickets.include_count)
    return request


@ app.post("/jinvoices/")
async def get_jinvoices(jinvoices: JobInvoices):
    info = jobInvoicesClass(jinvoices.jobid)

    request = tcr.getGridData(
        Grid=info.gridID,
        FilterConditions=info.filterConditions,
        QuickSearch=jinvoices.search,
        StartIndex=jinvoices.start_index,
        RecordCount=jinvoices.record_count,
        IncludeCount=jinvoices.include_count)
    return request


@ app.post("/tlabor/")
async def get_tlabor(tlabor: TicketLabor):
    info = ticketLaborClass(tlabor.ticketid)

    request = tcr.getGridData(
        Grid=info.gridID,
        FilterConditions=info.filterConditions,
        QuickSearch=tlabor.search,
        StartIndex=tlabor.start_index,
        RecordCount=tlabor.record_count,
        IncludeCount=tlabor.include_count)
    return request


@ app.post("/labortickets/")
async def get_labortickets(labortickets: LaborTickets):
    info = laborTicketClass()

    request = tcr.getGridData(
        Grid=info.gridID,
        FilterConditions=info.filterConditions,
        QuickSearch=labortickets.search,
        StartIndex=labortickets.start_index,
        RecordCount=labortickets.record_count,
        IncludeCount=labortickets.include_count)
    return request


@ app.post("/tsigns/")
async def get_tsigns(tsigns: TicketSigns):
    info = ticketSignsClass(tsigns.ticketid)

    request = tcr.getGridData(
        Grid=info.gridID,
        FilterConditions=info.filterConditions,
        QuickSearch=tsigns.search,
        StartIndex=tsigns.start_index,
        RecordCount=tsigns.record_count,
        IncludeCount=tsigns.include_count)
    return request


@ app.post("/trsigns/")
async def get_trsigns(trsigns: TicketReturnSigns):
    info = ticketReturnSignsClass(trsigns.ticketid)

    request = tcr.getGridData(
        Grid=info.gridID,
        FilterConditions=info.filterConditions,
        QuickSearch=trsigns.search,
        StartIndex=trsigns.start_index,
        RecordCount=trsigns.record_count,
        IncludeCount=trsigns.include_count)
    return request


@ app.post("/lineitems/")
async def get_lineitems(lineitems: LineItems):
    info = lineItemsClass()

    request = tcr.getGridData(
        Grid=info.gridID,
        FilterConditions=info.filterConditions,
        QuickSearch=lineitems.search,
        StartIndex=lineitems.start_index,
        RecordCount=lineitems.record_count,
        IncludeCount=lineitems.include_count)
    return request


@ app.post("/drivers/")
async def get_drivers(drivers: Drivers):
    info = driversClass()

    request = tcr.getGridData(
        Grid=info.gridID,
        FilterConditions=info.filterConditions,
        QuickSearch=drivers.search,
        StartIndex=drivers.start_index,
        RecordCount=drivers.record_count,
        IncludeCount=drivers.include_count)
    return request

@ app.post("/plistitems/")
async def get_plistitems(plistitems: PriceListItems):
    info = priceListItemsClass(
        PriceListID=plistitems.pricelistid,
        )

    request = tcr.getGridData(
        Grid=info.gridID,
        FilterConditions=info.filterConditions,
        QuickSearch=plistitems.search,
        StartIndex=plistitems.start_index,
        RecordCount=plistitems.record_count,
        IncludeCount=plistitems.include_count)
    return request

@ app.post("/pricelists/")
async def get_pricelists(pricelists: PriceLists):
    info = priceListsClass()

    request = tcr.getGridData(
        Grid=info.gridID,
        FilterConditions=info.filterConditions,
        QuickSearch=pricelists.search,
        StartIndex=pricelists.start_index,
        RecordCount=pricelists.record_count,
        IncludeCount=pricelists.include_count)
    return request
