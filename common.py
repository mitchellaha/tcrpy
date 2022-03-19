import datetime
import json
import math
import os

from dotenv import load_dotenv  # for Loading the .env Secrets

import login.getCookie as gc

load_dotenv()
email = os.getenv("email")
password = os.getenv("password")

with open("login/cookies.json") as f:
    cookies = json.load(f)
headers = gc.setHeaders(cookies, email, password)


gridDataUrl = "http://apps.tcrsoftware.com/tcr_2/webservices/data.asmx/GetGridData"


def findPages(recordCount, pageSize):
    """
    ### Finds the number of pages needed to display all records.

        Parameters:
            recordCount: The total number of records to display
            pageSize: The amount of records to load on each query

        Returns:
            The number of pages needed to display all records as an integer
    """
    pagesRounded = math.ceil(recordCount / pageSize)
    return pagesRounded


def startIndex(pageNumber, pageSize):
    """
    ### Function to find the start index of each page.

        Parameters:
            pageNumber: The page number to find the start index of
            pageSize: The amount of records to load on each query

        Returns:
            The start index of the page as an integer
    """
    return ((pageNumber - 1) * pageSize) + 1


def fixTime(timeString):
    """
    This function converts the time from the ticket into a datetime object.

    Parameters:
        string (str): The time string from the ticket.

    Returns:
        datetime (datetime): The datetime object.
    """
    splitString = timeString.split(".", 1)[0]
    fixedTime = datetime.datetime.strptime(splitString, '%Y-%m-%dT%H:%M:%S')
    return fixedTime


if __name__ == "__main__":
    print(headers)
