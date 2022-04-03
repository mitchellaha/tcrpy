# TCR-API
TCR API middleman using FastAPI

## To-Do:
- [ ] Cleanup Login / CookieGetter
- [ ] Add Status Filter to Customers & Jobs
- [ ] Add Descript Error Messages
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
