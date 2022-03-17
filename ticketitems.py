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



def TicketPayload(StartIndex, PageSize, Start=None, End=None):
    """
    This function creates the payload for the Ticket API call.

        Status:
            ALL: None
            Active: "A"
            Inactive: "I"
            On Hold: "H"
            Pre-Pay: "P"
    Parameters:
        Status (str): The status of the Ticket.
        StartIndex (int): The starting index of the Ticket.
        PageSize (int): The number of Tickets to return.

    Returns:
        payload (dict): The payload for the Ticket API call.

    """
    attributes = [
        "TicketID",
        "TicketType",
        "TicketID",
        "DriverName",
        "TruckCode",
        "TicketDate",
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


def getTicketData(StartIndex, PageSize, Start, End):
    """
    This function gets the Ticket data from the API.
    Parameters:
        startIndex (int): The starting index of the Ticket.
        pagesize (int): The number of Tickets to return.
        status (str): The status of the Ticket.

    Returns:
        count (int): The total number of Tickets.
        data (list): The list of Tickets.
    """
    payload = json.dumps(TicketPayload(StartIndex, PageSize, Start, End))
    response = requests.post(gridDataUrl, headers=headers, data=payload)
    # Loaded The D > Response From TCR
    resultjson = json.loads(json.loads(response.text)["d"]["Result"])
    count = resultjson["RecordCount"]
    data = resultjson["Data"]
    return count, data


def getTickets(Count, PageSize, Status):
    """
    This function gets all the Tickets from the API.
    Parameters:
        count (int): The total number of Tickets.
        status (str): The status of the Ticket.
        pagesize (int): The number of Ticket to return.

    Returns:
        data (list): The list of Ticket.
    """
    data = []
    for i in range(1, findPages(Count, PageSize) + 1):
        print("Page: " + str(i) + " of " + str(findPages(Count, PageSize)))
        post = getTicketData(startIndex(i, PageSize), PageSize, Status)
        data.extend(post[1])
    return data


if __name__ == "__main__":
    pass
