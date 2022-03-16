import datetime
import json
import os  # for os.path.basename
from pprint import pprint  # For debugging

import requests  # For making HTTP requests

from common import findPages, fixTime, gridDataUrl, startIndex, toJSON, headers
from tcr_py import gridCondition, gridSort

# import login.getCookie as gc
# with open("login/cookies.json") as f:
#     cookies = json.load(f)
# headers = gc.setHeaders(cookies)



def SchedulePayload(StartIndex, PageSize, Start=None, End=None):
    """
    This function creates the payload for the Schedule API call.

        Status:
            ALL: None
            Active: "A"
            Inactive: "I"
            On Hold: "H"
            Pre-Pay: "P"
    Parameters:
        Status (str): The status of the Schedule.
        StartIndex (int): The starting index of the Schedule.
        PageSize (int): The number of Schedules to return.

    Returns:
        payload (dict): The payload for the Schedule API call.

    """
    attributes = [
        "ScheduleID",
        "ScheduleType",
        "TicketID",
        "DriverName",
        "TruckCode",
        "ScheduleDate",
        "ClockIn",
        "TimeNeeded",
        "TimeSetBy",
        "EstimatedTimeOnSite",
        "Status",
        "TicketNumber",
        "PrintStatus",
        "Description",
        "Comments",
        "CustomerCode",
        "CustomerName",
        "JobNumber",
        "JobAddress1",
        "City",
        "Foreman",
        "ForemanPhone",
        "DispatcherName",
        "JobName",
        "ProjectManagerName",
        "PONumber",
        "ForemanCompany",
        "StartAddress",
        "EndAddress"
    ]
    conditions = []
    if Start is not None:
        conditions.append(gridCondition(
            attribute="StartDate", operator=6, v1=Start).dict())

    if End is not None:
        conditions.append(gridCondition(
            attribute="EndDate", operator=6, v1=End).dict())

    conditions.append(gridCondition(
        attribute="BranchID", operator=1, v1="").dict())
    conditions.append(gridCondition(
        attribute="Status", operator=1, v1="").dict())
    conditions.append(gridCondition(
        attribute="TransactionID", operator=1, v1="").dict())
    conditions.append(gridCondition(
        attribute="RecordType", operator=1, v1=1).dict())

    sort = gridSort("TimeSetBy", order=1).list()

    payload = {
        "query": {
            "GridID": 54,
            "Attributes": attributes,
            "Filter": {
                "Conditions": conditions
            },
            "Sort": sort,
            "CustomSort": None,
            "StartIndex": StartIndex,
            "RecordCount": PageSize
        }}
    return payload


def getScheduleData(StartIndex, PageSize, Start, End):
    """
    This function gets the Schedule data from the API.
    Parameters:
        startIndex (int): The starting index of the Schedule.
        pagesize (int): The number of Schedules to return.
        status (str): The status of the Schedule.

    Returns:
        count (int): The total number of Schedules.
        data (list): The list of Schedules.
    """
    payload = json.dumps(SchedulePayload(StartIndex, PageSize, Start, End))
    response = requests.post(gridDataUrl, headers=headers, data=payload)
    # Loaded The D > Response From TCR
    resultjson = json.loads(json.loads(response.text)["d"]["Result"])
    count = resultjson["RecordCount"]
    data = resultjson["Data"]
    return count, data


def getSchedules(Count, PageSize, Status):
    """
    This function gets all the Schedules from the API.
    Parameters:
        count (int): The total number of Schedules.
        status (str): The status of the Schedule.
        pagesize (int): The number of Schedule to return.

    Returns:
        data (list): The list of Schedule.
    """
    data = []
    for i in range(1, findPages(Count, PageSize) + 1):
        print("Page: " + str(i) + " of " + str(findPages(Count, PageSize)))
        post = getScheduleData(startIndex(i, PageSize), PageSize, Status)
        data.extend(post[1])
    return data


if __name__ == "__main__":
    pass
