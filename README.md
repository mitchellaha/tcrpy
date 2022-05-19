# TCRAPI
[![PyPI Version](https://img.shields.io/pypi/v/TCRAPI)](https://pypi.org/project/TCRAPI/)
[![Python Versions](https://img.shields.io/pypi/pyversions/TCRAPI)](https://pypi.org/project/TCRAPI/)

TCR API Interaction Library

## Usage

- **[QuickStart](docs/quickstart.md)**

- **[References](docs/references.md)**

- **[FastAPI](docs/FastAPI.md)**



## Install

### via pip ( recommended )

The easiest way to install the latest version from PyPI is by using [pip](https://pip.pypa.io/):

```$ pip install TCRAPI```

### via Git Clone *with extras* 

1. Clone the repository to an empty directory
    - ```$ git clone https://github.com/mitchellaha/TCRAPI.git .```
2. Create a virtual environment
    - ```$ python3 -m venv venv```
3. Activate the virtual environment
    - ```$ source venv/bin/activate```
4. Install dependencies
    - ```$ pip install -r requirements.txt```

### Build From Source ( *Advanced* )

1. Clone the repository to an empty directory
    - ```$ git clone https://github.com/mitchellaha/TCRAPI.git .```
2. Verify SetupTools is Updated
    - ```$ pip install --upgrade setuptools```
3. Install dependencies

-------------------

# To-Do:
- [ ] Add more documentation
- [x] Add Status Filter to Customers & Jobs
- [ ] *Create More Unified Filter Conditions*
    - [ ] GetSideMenus contains info for Quick Filter Check Boxes
    - [ ] Pull the needed data from the TCR_Menu/TCRConstants
    - [ ] Advanced Search Filters:
        - DataTypes = "QueryFilterFieldDataType" in TCRConstants
        - Each DataType is allowed certain "QueryParamOperator" in TCRConstants
- [ ] Add Ticket Status & Ticket Type Filter
- [x] Pagination Support
- [x] Cleanup Login / CookieGetter
- [ ] Serverside Logging
- [ ] Add Descript Response Error Messages
- [ ] Add Authentication

- [ ] **[All GetGridData](docs/quickstart.md)**

#### Other
- [x] Get Side Menus
- [ ] *Get Search Records*
- [x] Get Grid Columns For Advanced Search
- [ ] Customers Page
    - [ ] Get Tickets Count
    - [ ] Get Customer Overview
    - [ ] Get Billing History
    - [ ] Get Top 5 Equipment
- [ ] Get Audit Data
    - [ ] Customers
    - [ ] Jobs
    - [ ] Tickets
