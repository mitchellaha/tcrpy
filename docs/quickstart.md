# QuickStart

# Base Quick Reference

### Create a TCR API Client  
**tcrClient** class will be used for all TCR Rest API interactions.  
**tcrAuth** class Needs to be created to hand the tcrClient the correct headers with authentication cookies.  


```python
import TCRAPI

tcrAuth = TCRAPI.auth(
    email="email@youremail.com",
    password="yourpassword"
)

tcrClient = TCRAPI.api(
    headers=tcrAuth.header,
)
```

### Get Customer Grid Data

```python
from TCRAPI.getgriddata import customersClass

customerGridInfo = customersClass()

getCustomersGrid = tcr.getGridData(
    Grid=customersGridInfo.gridID,
    FilterConditions=customersGridInfo.filterConditions,
    StartIndex=1, # Optional - Default is 1 - Used for Pagination
    RecordCount=250,  # Optional - Default is 250 - Min 50 Max 250
    QuickSearch=QuickSearchQuery,  # Optional
    IncludeCount=True  # Optional - Default is True
)

count = getCustomersGrid["count"]  # Total number of records : int
data = getCustomersGrid["data"]  # List of dictionaries

```


# Examples

### Get Customers with Search Query
```python
from TCRAPI import auth  # Imports the auth module
from TCRAPI import api  # Imports the api module

tcrAuth = auth(
    email="email@youremail.com",
    password="yourPassword"
)
tcr = api(
    headers=tcrAuth.headers,
)

from TCRAPI.getgriddata import customersClass

customersGridInfo = customersClass()

QuickSearchQuery = "Example Customer"

getCustomersGrid = tcr.getGridData(
    Grid=customersGridInfo.gridID,
    FilterConditions=customersGridInfo.filterConditions,
    StartIndex=1, # Optional - Default is 1 - Used for Pagination
    RecordCount=250,  # Optional - Default is 250 - Min 50 Max 250
    QuickSearch=QuickSearchQuery,  # Optional
    IncludeCount=True  # Optional - Default is True
)

count = getCustomersGrid["count"]  # Total number of records : int
data = getCustomersGrid["data"]  # List of dictionaries

print("total customers: " + str(count))

print(data)

```
