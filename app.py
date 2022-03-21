from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from driverschedule import scheduleOBJ
from ticket_items import tItemsOBJ

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
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
            "end": "MM/DD/YYYY"
        },
    },
    "ticket_items": {
        "type": "post",
        "url": "/titems/",
        "parameters": {
            "ticketid": "2613496"
        },
    }
}

class Schedule(BaseModel):
    start: str
    end: str

class TicketItems(BaseModel):
    ticketid: int


@app.get("/")
def read_root():
    return definitions


@app.post("/schedule/")
async def get_schedule(schedule: Schedule):
    start = schedule.start
    end = schedule.end
    # schedule = getSchedule(start, end)
    schedule = scheduleOBJ().getSchedule(start, end)
    count = schedule[0]
    data = schedule[1]
    return {"count": count, "data": data}


@app.post("/titems/")
async def get_items(items: TicketItems):
    ticketid = items.ticketid
    response = tItemsOBJ().getTicketItems(ticketID=ticketid)
    count = response[0]
    data = response[1]
    return {"count": count, "data": data}
