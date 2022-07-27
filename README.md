# tcrpy
[![PyPI Version](https://img.shields.io/pypi/v/TCRAPI)](https://pypi.org/project/TCRAPI/)
[![Python Versions](https://img.shields.io/pypi/pyversions/TCRAPI)](https://pypi.org/project/TCRAPI/)

Python Library for Interacting with the TCR Platform API.

## Usage

- **[QuickStart](docs/quickstart.md)**

- **[References](docs/references.md)**

- **[FastAPI](docs/FastAPI.md)**

- **[Release ChangeLog](docs/changelog.md)**



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

### From Source ( *Advanced* )

1. Clone the repository to an empty directory
    - ```$ git clone https://github.com/mitchellaha/TCRAPI.git .```
2. Verify SetupTools is Updated
    - ```$ pip install --upgrade setuptools```
3. Install the project
    - ```$ python setup.py install```


-------------------


## To-Do:
- [ ] **[All TCR API Endpoints](docs/TCREndpoints.md)**
- [ ] Add more documentation
    - [ ] Explain Correlation & Uses of different TCR Rest endpoints
- [x] *Create More Unified Filter Conditions*
    - [x] ~~Add Status Filter to Customers & Jobs~~
    - [ ] GetSideMenus contains info for Quick Filter Check Boxes
        - [ ] Add Ticket Status & Ticket Type Filter
    - [ ] Pull the needed data from the TCR_Menu/TCRConstants
    - [ ] Advanced Search Filters:
        - [ ] Python Class Enums with TCRConstants
        - DataTypes = "QueryFilterFieldDataType" in TCRConstants
        - Each DataType is allowed certain "QueryParamOperator" in TCRConstants
- [x] Pagination Support
- [x] Cleanup Login / CookieGetter


- [ ] **[FastAPI](docs/FastAPI.md)**
    - [x] Add Documentation
        - [ ] Add PostMan Collection
    - [ ] Add Authentication
    - [ ] Serverside Logging
    - [ ] Add Descript Error Messages
