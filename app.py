from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from tcr_interactions import post_models, get_grid, get_user_settings
from tcr_data_calls.GetGridData import getGridData
from tcr_data_calls.DriverSchedule import driverScheduleClass
from tcr_data_calls.TicketItems import ticketItemsClass
from tcr_data_calls.CustomerJobs import customerJobsClass

app = FastAPI()

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
    "schedule": {
        "type": "post",
        "url": "/schedule/",
        "parameters": {
            "start": "MM/DD/YYYY",
            "end": "MM/DD/YYYY",
            "include_count": True
        },
    },
    "ticket_items": {
        "type": "post",
        "url": "/titems/",
        "parameters": {
            "ticketid": "2613496",
            "include_count": False
        },
    },
    "get_Grid": {
        "type": "post",
        "url": "/getgrid/",
        "parameters": {
            "grid": 1
        },
    },
    "get_grid_settings": {
        "type": "post",
        "url": "/getgridsettings/",
        "parameters": {
            "grid": 1
        },
    },
    "customer_jobs": {  # !TODO: Add this to the API
        "type": "post",
        "url": "/cjobs/",
        "parameters": {
            "customerid": "2613496",
            "include_count": False
        },
    },
}


class GetGrid(BaseModel):
    grid: int


class GetGridSettings(BaseModel):
    grid: int


class Schedule(BaseModel):
    start: str
    end: str
    include_count: bool = False


class TicketItems(BaseModel):
    ticketid: int
    include_count: bool = False

class CustomerJobs(BaseModel):
    customerid: int
    include_count: bool = False


# ! Basic Info Function
@ app.get("/")
def read_root():
    return definitions

# ! Basic Info Function
@ app.post("/getgrid/")  # ? Returns the Full GetGrid Post of TCR
async def get_gridPost(grid: GetGrid):
    grid = grid.grid
    response = get_grid.getGrid(grid)
    return response

# ! Basic Info Function
@ app.post("/getgridsettings/")  # ? Returns the Full GetGridSettings Post of TCR
async def get_gridSettingsPost(grid: GetGridSettings):
    grid = grid.grid
    response = get_user_settings.getGridSettings(grid)
    return response



@ app.post("/schedule/")
async def get_schedule(schedule: Schedule):
    scheduleClass = driverScheduleClass(schedule.start, schedule.end)
    request = getGridData(scheduleClass.gridID, scheduleClass.filterConditions)
    if schedule.include_count is True:
        return {"count": request[0], "data": request[1]}
    else:
        return request[1]


@ app.post("/titems/")  # ? Returns the Items for the Provided Ticket
async def get_items(items: TicketItems):
    tItemsClass = ticketItemsClass(items.ticketid)
    request = getGridData(tItemsClass.gridID, tItemsClass.filterConditions)
    if items.include_count is True:
        return {"count": request[0], "data": request[1]}
    else:
        return request[1]


@ app.post("/cjobs/")
async def get_cjobs(cjobs: CustomerJobs):
    cJobsClass = customerJobsClass(cjobs.customerid)
    request = getGridData(cJobsClass.gridID, cJobsClass.filterConditions)
    if cjobs.include_count is True:
        return {"count": request[0], "data": request[1]}
    else:
        return request[1]
