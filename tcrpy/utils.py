import math
import datetime as dt

def millisecond_stamp_to_datetime(milliseconds: int):  # ? As much as i would like to move this to datetime_utils, id rather handlers be independent
    """
    Convert milliseconds to datetime object removing the "/Date(...)/"
    """
    seconds = int("".join([x for x in milliseconds if x.isdigit()])) / 1000  # Remove the "/Date(...)/" and convert to seconds
    return dt.datetime.fromtimestamp(seconds) + dt.timedelta(hours=1)  # Add 1 Hour Since TCR is off by 1 hour

def page_count(recordCount, pageSize):
    """
    ### Finds the number of pages needed to display all records.

        Parameters:
            recordCount: The total number of records
            pageSize: The amount of records to load on each query

        Returns:
            The number of pages needed to display all records as an integer
    """
    return math.ceil(recordCount / pageSize)


def start_index(pageNumber, pageSize):
    """
    ### Function to find the start index of each page.

        Parameters:
            pageNumber: The page number to find the start index of
            pageSize: The amount of records to load on each query

        Returns:
            The start index of the page as an integer
    """
    return ((pageNumber - 1) * pageSize) + 1
