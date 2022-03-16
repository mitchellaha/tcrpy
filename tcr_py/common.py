import json
import os  # for os.path.basename
from pprint import pprint  # For debugging

import requests  # For making HTTP requests
from dotenv import load_dotenv  # for Loading the .env Secrets
# from pymongo import MongoClient  # Import MongoDB for MongoDB Connection
load_dotenv()

"""
dbGetGrid = MongoDB Collection That Will Store All Grids and Their Respective Information. Database Name: 'getgrid' ; From TCR .../tcr_2/webservices/config.asmx/GetGrid
headers = Headers for HTTP Requests to TCR. May Be Moved In the Future.
"""
# dbGetGrid = MongoClient(os.getenv('mongoURL')).tcrinfo.getgrid
urlGetGridData = "http://apps.tcrsoftware.com/tcr_2/webservices/data.asmx/GetGridData"
urlGetGridID = "http://apps.tcrsoftware.com/tcr_2/webservices/config.asmx/GetGridByID"
headers = {
    'DNT': '1',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    'Content-Type': 'application/json; charset=utf-8',
    'Accept': 'application/json',
    'Cookie': str(os.getenv('token'))
    }


# print(str(os.getenv('token')))
