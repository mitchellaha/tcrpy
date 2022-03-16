import datetime
import json
import math
import os

from dotenv import load_dotenv  # for Loading the .env Secrets
import login.getCookie as gc

load_dotenv()


with open("login/cookies.json") as f:
    cookies = json.load(f)
headers = gc.setHeaders(cookies)

gridDataUrl = "http://apps.tcrsoftware.com/tcr_2/webservices/data.asmx/GetGridData"

# This Checks If The Document Within the Collection Exists then returns true or false.
def alreadyExists(collect, key, value):
    if collect.find({key: value}).count() > 0:
        return True
    else:
        return False


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


def toJSON(data, filename):
    """
    ### This function converts the data to a JSON file.
        toJSON(data, "data/tickets.json")
    """
    with open(filename, "w") as outfile:
        json.dump(data, outfile, indent=4, default=str)
    print("JSON Created")


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
    # # Total Records / Customers
    # RecordCount = 2992

    # # Amount To Show on Each Page / Amount To Load on Each Query
    # pageSize = 250

    # # Find the number of pages needed to display all records
    # pages = findPages(RecordCount, pageSize)

    # # Find The Start Index of Each Page 5 and page 6 for a page size of 250 Records Per Page
    # print("Page 5 Start Index: " + str(startIndex(5, pageSize)))
    # print("Page 6 Start Index: " + str(startIndex(6, pageSize)))

    # '''
    # Examples Of StartIndex for a 250 Page Size:
    # Page 1 Start Index: 1
    # Page 2 Start Index: 251
    # Page 3 Start Index: 501
    # Page 4 Start Index: 751
    # Page 5 Start Index: 1001
    # Page 6 Start Index: 1251
    # '''
