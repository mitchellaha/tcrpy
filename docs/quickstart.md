# QuickStart

> In Progress.....

# Base Quick Reference

### Create a TCR API Client  
**tcrClient** class will be used for all TCR Rest API interactions.  

# Examples

```python
from TCRAPI import api  # Imports the api module
from TCRAPI.models import Filter

tcr = api(
    email="email@youremail.com",
    password="yourPassword"
)

filterExample = Filter(
    attribute="JobID",
    operator=1,
    values=[958555]
).dict()

getCustomersGrid = tcr.getGridData(
    Grid=4,
    FilterConditions=filterExample,
    StartIndex=1, # Optional - Default is 1 - Used for Pagination
    RecordCount=250,  # Optional - Default is 250 - Min 50 Max 250
    QuickSearch=None,  # Optional
    IncludeCount=True  # Optional - Default is True
)

count = getCustomersGrid["count"]  # Total number of records : int
data = getCustomersGrid["data"]  # List of dictionaries

print("total customers: " + str(count))

print(data)

```
