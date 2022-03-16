from fastapi import FastAPI
from pydantic import BaseModel
from driverschedule import getScheduleData

app = FastAPI()

# Directory and Functions of API as a Dictionary to be Served to Root
definitions = {
    "Purpose": "Each Endpoint Shown Below is a Function of the API with the data needed",
    "schedule": {
        "start": "MM/DD/YYYY",
        "end": "MM/DD/YYYY"
    },
    "items": {
        "ticketid": "2613496"
    }
}

def getSchedule(start, end):
    return getScheduleData(1, 100, start, end)

class Schedule(BaseModel):
    start: str
    end: str

class Items(BaseModel):
    ticketid: int


@app.get("/")
def read_root():
    return definitions

@app.post("/schedule/")
async def get_schedule(schedule: Schedule):
    start = schedule.start
    end = schedule.end
    schedule = getSchedule(start, end)
    count = schedule[0]
    data = schedule[1]
    return {"count": count, "data": data}

@app.get("/test")
async def scheduleTest():
    start = "03/17/2022"
    end = "03/17/2022"
    schedule = getSchedule(start, end)
    count = schedule[0]
    data = schedule[1]
    return {"count": count, "data": data}
