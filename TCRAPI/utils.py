import datetime
import math
from TCRAPI.models import *


def getGridDataQuickSearch(SearchQuery, GridFilterConditions, QuickSearchFieldsList):
    def createConditionsModelForSearch(field, value):
        return ConditionsModel(
            Attribute=field,
            Values=[value],
            Operator=10
        )

    searchConditions = [createConditionsModelForSearch(field, SearchQuery) for field in QuickSearchFieldsList]

    return FilterModel(
        Conditions=GridFilterConditions,
        Filter=FilterSearchConditionsModel(
            Conditions=searchConditions,
            GroupOperator=2
        )
    )

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
