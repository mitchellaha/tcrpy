# Changelog

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
