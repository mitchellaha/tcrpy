from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Union, List

from tcr_interactions.TCR import TCRAPI
from getgriddata.Customers import customersClass
# from getgriddata.Jobs import jobsClass
# from getgriddata.JobTickets import jobTicketsClass
# from getgriddata.JobInvoices import jobInvoicesClass
# from getgriddata.CustomerContacts import customerContactsClass
# from getgriddata.CustomerInvoices import customerInvoicesClass
# from getgriddata.CustomerJobs import customerJobsClass
# from getgriddata.DriverSchedule import driverScheduleClass
# from getgriddata.InvoiceDetails import invoiceDetailsClass
# from getgriddata.TicketItems import ticketItemsClass
# from getgriddata.TicketLabor import ticketLaborClass
# from getgriddata.LaborTickets import laborTicketClass
# from getgriddata.TicketSigns import ticketSignsClass
# from getgriddata.TicketReturnSigns import ticketReturnSignsClass
# from getgriddata.LineItems import lineItemsClass
# from getgriddata.Drivers import driversClass
# from getgriddata.Invoices import invoicesClass
# from tcr_interactions import get_grid, get_user_settings
# from tcr_interactions.get_grid_data import getGridData


tcr = TCRAPI()

app = FastAPI(
    title="TCR-API",
    description="An API middleware TCR"
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
}


class GetGrid(BaseModel):
    grid: int

class GetGridSettings(BaseModel):
    grid: int

class GetGridBaseModel(BaseModel):
    include_count: Optional[bool]

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
    search: Optional[str]
    status: Optional[Union[str, List[str]]]

class Jobs(GetGridBaseModel):
    search: Optional[str]
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
    search: Optional[str]

class Drivers(GetGridBaseModel):
    search: Optional[str]

class Invoices(GetGridBaseModel):
    search: Optional[str]


# ! Basic Info Function
@ app.get("/")
def read_root():
    return definitions

# ! Basic Info Function
@ app.post("/getgrid/")  # ? Returns the Full GetGrid Post of TCR
async def get_gridPost(grid: GetGrid):
    grid = grid.grid
    response = tcr.getGrid(grid)
    return response

# ! Basic Info Function
@ app.post("/getgridsettings/")  # ? Returns the Full GetGridSettings Post of TCR
async def get_gridSettingsPost(grid: GetGridSettings):
    grid = grid.grid
    response = tcr.getGridSettings(grid)
    return response



# @ app.post("/schedule/")
# async def get_schedule(schedule: Schedule):
#     scheduleClass = driverScheduleClass(schedule.start, schedule.end)
#     request = tcr.getGridData(scheduleClass.gridID, scheduleClass.filterConditions)
#     if schedule.include_count is True:
#         return {"count": request[0], "data": request[1]}
#     else:
#         return request[1]


# @ app.post("/titems/")  # ? Returns the Items for the Provided Ticket
# async def get_items(items: TicketItems):
#     tItemsClass = ticketItemsClass(items.ticketid)
#     request = tcr.getGridData(tItemsClass.gridID, tItemsClass.filterConditions)
#     if items.include_count is True:
#         return {"count": request[0], "data": request[1]}
#     else:
#         return request[1]


# @ app.post("/cjobs/")
# async def get_cjobs(cjobs: CustomerJobs):
#     cJobsClass = customerJobsClass(cjobs.customerid)
#     request = tcr.getGridData(cJobsClass.gridID, cJobsClass.filterConditions)
#     if cjobs.include_count is True:
#         return {"count": request[0], "data": request[1]}
#     else:
#         return request[1]


# @ app.post("/cinvoices/")
# async def get_cinvoices(cinvoices: CustomerInvoices):
#     cInvoicesClass = customerInvoicesClass(cinvoices.customerid)
#     request = tcr.getGridData(cInvoicesClass.gridID, cInvoicesClass.filterConditions)
#     if cinvoices.include_count is True:
#         return {"count": request[0], "data": request[1]}
#     else:
#         return request[1]


# @ app.post("/idetails/")
# async def get_idetails(idetails: InvoiceDetails):
#     iDetailsClass = invoiceDetailsClass(idetails.invoiceid)
#     request = tcr.getGridData(iDetailsClass.gridID, iDetailsClass.filterConditions)
#     if idetails.include_count is True:
#         return {"count": request[0], "data": request[1]}
#     else:
#         return request[1]

# @ app.post("/ccontacts/")
# async def get_ccontacts(ccontacts: CustomerContacts):
#     cContactsClass = customerContactsClass(ccontacts.customerid)
#     request = tcr.getGridData(cContactsClass.gridID, cContactsClass.filterConditions)
#     if ccontacts.include_count is True:
#         return {"count": request[0], "data": request[1]}
#     else:
#         return request[1]

@ app.post("/customers/")
async def get_customers(customers: Customers):
    cCustomersClass = customersClass()
    if customers.status:
        cCustomersClass.setStatusFilter(customers.status)
    if customers.search:
        searchFilter = cCustomersClass.search(customers.search)
        cCustomersClass.filterConditions = searchFilter
    request = tcr.getGridData(cCustomersClass.gridID, cCustomersClass.filterConditions)
    if customers.include_count is True:
        return {"count": request[0], "data": request[1]}
    else:
        return request[1]

# @ app.post("/jobs/")
# async def get_jobs(jobs: Jobs):
#     jJobsClass = jobsClass()
#     if jobs.status:
#         jJobsClass.setStatusFilter(jobs.status)
#     if jobs.search:
#         searchFilter = jJobsClass.search(jobs.search)
#         jJobsClass.filterConditions = searchFilter
#     request = tcr.getGridData(jJobsClass.gridID, jJobsClass.filterConditions)
#     if jobs.include_count is True:
#         return {"count": request[0], "data": request[1]}
#     else:
#         return request[1]

# @ app.post("/jtickets/")
# async def get_jtickets(jtickets: JobTickets):
#     jTicketsClass = jobTicketsClass(jtickets.jobid)
#     request = tcr.getGridData(jTicketsClass.gridID, jTicketsClass.filterConditions)
#     if jtickets.include_count is True:
#         return {"count": request[0], "data": request[1]}
#     else:
#         return request[1]

# @ app.post("/jinvoices/")
# async def get_jinvoices(jinvoices: JobInvoices):
#     jInvoicesClass = jobInvoicesClass(jinvoices.jobid)
#     request = tcr.getGridData(jInvoicesClass.gridID, jInvoicesClass.filterConditions)
#     if jinvoices.include_count is True:
#         return {"count": request[0], "data": request[1]}
#     else:
#         return request[1]

# @ app.post("/tlabor/")
# async def get_tlabor(tlabor: TicketLabor):
#     tLaborClass = ticketLaborClass(tlabor.ticketid)
#     request = tcr.getGridData(tLaborClass.gridID, tLaborClass.filterConditions)
#     if tlabor.include_count is True:
#         return {"count": request[0], "data": request[1]}
#     else:
#         return request[1]

# @ app.post("/labortickets/")
# async def get_labortickets(labortickets: LaborTickets):
#     lTicketClass = laborTicketClass()
#     request = tcr.getGridData(lTicketClass.gridID, lTicketClass.filterConditions)
#     if labortickets.include_count is True:
#         return {"count": request[0], "data": request[1]}
#     else:
#         return request[1]

# @ app.post("/tsigns/")
# async def get_tsigns(tsigns: TicketSigns):
#     tSignsClass = ticketSignsClass(tsigns.ticketid)
#     request = tcr.getGridData(tSignsClass.gridID, tSignsClass.filterConditions)
#     if tsigns.include_count is True:
#         return {"count": request[0], "data": request[1]}
#     else:
#         return request[1]

# @ app.post("/trsigns/")
# async def get_trsigns(trsigns: TicketReturnSigns):
#     tRSignsClass = ticketReturnSignsClass(trsigns.ticketid)
#     request = tcr.getGridData(tRSignsClass.gridID, tRSignsClass.filterConditions)
#     if trsigns.include_count is True:
#         return {"count": request[0], "data": request[1]}
#     else:
#         return request[1]

# @ app.post("/lineitems/")
# async def get_lineitems(lineitems: LineItems):
#     lItemsClass = lineItemsClass()
#     if lineitems.search:
#         searchFilter = lItemsClass.search(lineitems.search)
#         lItemsClass.filterConditions = searchFilter
#     request = tcr.getGridData(lItemsClass.gridID, lItemsClass.filterConditions)
#     if lineitems.include_count is True:
#         return {"count": request[0], "data": request[1]}
#     else:
#         return request[1]

# @ app.post("/drivers/")
# async def get_drivers(drivers: Drivers):
#     dDriversClass = driversClass()
#     if drivers.search:
#         searchFilter = dDriversClass.search(drivers.search)
#         dDriversClass.filterConditions = searchFilter
#     request = tcr.getGridData(dDriversClass.gridID, dDriversClass.filterConditions)
#     if drivers.include_count is True:
#         return {"count": request[0], "data": request[1]}
#     else:
#         return request[1]

# @ app.post("/invoices/")
# async def get_invoices(invoices: Invoices):
#     iInvoicesClass = invoicesClass()
#     if invoices.search:
#         searchFilter = iInvoicesClass.search(invoices.search)
#         iInvoicesClass.filterConditions = searchFilter
#     request = tcr.getGridData(iInvoicesClass.gridID, iInvoicesClass.filterConditions)
#     if invoices.include_count is True:
#         return {"count": request[0], "data": request[1]}
#     else:
#         return request[1]
