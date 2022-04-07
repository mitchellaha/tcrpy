# TCR-API
TCR API middleman using FastAPI

## To-Do:
- [x] Add Status Filter to Customers & Jobs
- [ ] Create More Unified Filter Conditons
    - [ ] Pull the needed data from the TCR_Menu
- [ ] Add Ticket Status & Ticket Type Filter
- [ ] Pagination Support
- [x] Cleanup Login / CookieGetter
- [ ] Serverside Logging
- [ ] Add Descript Response Error Messages
- [ ] Add Authentication


## Install
1. Create a virtual environment
    - ```$ python3 -m venv venv```
2. Activate the virtual environment
    - ```$ source venv/bin/activate```
3. Install dependencies
    - ```$ pip install -r requirements.txt```
4. Add Login Information to enviroment variables or .env file
    - ```$ export email=<"email">```
    - ```$ export password=<"password">```
4. Run the application
    - ```$ uvicorn app:app --reload```


## Working TCR Requests

#### Get Grid Data
- [x] Customers
    - [x] Customer Contacts
    - [x] Customer Invoices
    - [x] Customer Jobs
- [x] Jobs
    - [x] *Job Tickets*
    - [x] *Job Invoices*
    - [ ] Job TCPs
    - [ ] Job Photos
    - [ ] Quanitity On Hand
- [ ] Labor
    - [x] *Labor Tickets*?
        - [ ] Add a search by Certified and Dates
    - [ ] Labor Misc Time
    - [x] Drivers Schedule
- [ ] Tickets
    - [x] Ticket Items
    - [ ] Ticket TCPs
    - [ ] Ticket Misc Items
    - [x] *Ticket Labor*
    - [x] *Ticket Signs*
    - [x] *Ticket Return Signs*
    - [ ] Ticket Ticket Kits
- [ ] Invoices
    - [x] Invoice Details
- [ ] Quotes
    - [ ] Quote Items
    - [ ] Quote Signs
- [ ] Item Tracking
- [ ] *Line Items*
    - [ ] Line Item Price List
- [ ] Sub Items
- [ ] Signs
- [ ] *Drivers*
- [ ] Equipment
- [ ] Trucks
- [ ] Zones
- [ ] Labels
- [ ] Price Lists
- [ ] Quote Extras

#### Other
- [ ] *Get Side Menuss*
- [ ] Get Tickets Count
- [ ] Get Customer Overview
- [ ] Get Billing History
- [ ] Get Top 5 Equipment
- [ ] Get Audit Data
    - [ ] Customers
    - [ ] Jobs
    - [ ] Tickets
