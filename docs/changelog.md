# Changelog

## [0.2.9.1] - 2022-12-15
- Removed Print Statement from getgriddata

## [0.2.9] - 2022-12-15
- **Added** - GetGrid Data custom attributes + Sort parameter

## [0.2.8] - 2022-11-03
- Fixed: Negative TimeStamps breaking datetime conversions on millisecond_stamp_to_datetime

## [0.2.7] - 2022-11-03
- Fixed: getDrivers & getEmployees now correctly converts DateTimes

## [0.2.6] - 2022-11-02
- *Change*: getItems dates converted to Datetime

## [0.2.5] - 2022-10-25
- *Change*: getSubItems, getEquipment, getEmployees, getDrivers dates converted to Datetime
- Fixed: 0.2.3 & 0.2.4 Conflict

## [0.2.4] - 2022-10-25
- **Added** - getSubItems, getEquipment, getEmployees, getDrivers

## [0.2.3] - 2022-10-25
- **Added** - getPriceLists, getPriceListItem, getInvoiceItemPrice, getNewItemForQuote


## [0.2.2] - 2022-01-27
- **Added**: GetCustomer, GetJob, GetTicket all return dates as datetime objects
- **Added**: datetime_to_string utility function

## [0.2.1] - 2022-01-27
- **Added**: GetGridData now converts date strings to datetime objects
- Fixed: GetGridSortSettings

## [0.2.0] - Complete Rewrite of Filter Handling
- **Added**: TCRAPI.utils.millisecond_stamp_to_datetime() function
- **Added**: GridInfo.json docs containing grid info
- *Change*: TCRAPI.auth() no longer needs to be handed over to TCRAPI.api()
- Removed: TCRAPI.GetGridData folder - see GridInfo.json for replacement
- Removed: config.py as it was empty


## [0.1.2] - 2022-06-28
- *Change*: GetGridData Class ID & Name are Now Constants
- *Change*: Search Models Now Work Better and Usage is more Clear

## [0.1.1] - 2022-??-??
- **Added**: Single Customer Endpoint
- **Added**: Single Ticket Endpoint
- **Added**: Single Job Endpoint
- **Added**: Get Items Endpoint
- **Added**: Company Info Endpoint
- *Change*: Better Inline Documentation
- *Change*: Hard Defined List Models
- *Change*: GetGridData Cleaned Up & More Functional


## [0.1.0] - Initial release  
- **First PyPi Release!**
