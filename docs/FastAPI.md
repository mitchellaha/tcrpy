# Demo Using FastAPI

For Reference- **[FastAPI Library Documatation](https://fastapi.tiangolo.com/)**

## via Git Clone

1. Clone the repository
    - ```$ git clone https://github.com/mitchellaha/TCRAPI.git```
2. Create a virtual environment
    - ```$ python3 -m venv venv```
3. Activate the virtual environment
    - ```$ source venv/bin/activate```
4. Install dependencies
    - ```$ pip install -r requirements.txt```
5. Add Login Information to environment variables or .env file
    - **Environment Variables**
        - ```$ export email=<"email">```
        - ```$ export password=<"password">```
    - **.env File**

            email = "<email>"
            password = "<password>"

6. Run the application
    - ```$ uvicorn app:app --reload```