from .tcr_post import tcrPost, getGridID
from .common import *


def getGridByID(gridID: int):
    payload = {
        "gridID": gridID
        }
    paydata = tcrPost(payload=payload, tcrurl=getGridID).request()
    tcrResponse = paydata  # Loads the JSON Response
    return tcrResponse
