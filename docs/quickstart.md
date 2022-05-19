# QuickStart


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
