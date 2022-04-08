import os

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv  # for Loading the .env Secrets


class tcrAuth:
    """
    email and password are set from env variables
    """
    load_dotenv()

    def __init__(self):
        self.email = os.getenv("email")
        self.password = os.getenv("password")
        self.cookie = None
        self.cookie_expiration = None  # todo: may eventually need to add a get new cookie function
        self.headers = None

    def setLogin(self, email: str, password: str):
        self.email = email
        self.password = password

    def setCookie(self, cookies: dict):
        self.cookie = cookies

    def setCookieExpiration(self, expire: dict):
        self.cookie_expiration = expire

    def setHeaders(self, cookies):
        headers = {
            'DNT': '1',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json'
        }
        cookie = "Email={}; ASP.NET_SessionId={}; TCRAuth={}".format(cookies["Email"], cookies["ASP.NET_SessionId"], cookies["TCRAuth"])
        headers["Cookie"] = cookie
        self.headers = headers

    def getCookies(self):
        """
        Returns TCR cookies[0] and expiration[1]
        """
        with requests.Session() as s:
            loginURL = "http://apps.tcrsoftware.com/tcr_2/login.aspx"

            s.headers.update(
                {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
            )
            page = s.get(loginURL)

            # Rip the form data from the page with BS4.
            soup = BeautifulSoup(page.content, 'html.parser')
            viewState = soup.select_one("#__VIEWSTATE")["value"]
            viewStateGenerator = soup.select_one(
                "#__VIEWSTATEGENERATOR")["value"]
            eventValidation = soup.select_one("#__EVENTVALIDATION")["value"]

            newHeaders = {
                "X-MicrosoftAjax": "Delta=true",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://apps.tcrsoftware.com/tcr_2/login.aspx"
            }

            requestData = {
                "ScriptManager1": "UpdatePanel1|BtnSubmit",
                "__LASTFOCUS": "",
                "__EVENTTARGET": "",
                "__EVENTARGUMENT": "",
                "__VIEWSTATE": str(viewState),
                "__VIEWSTATEGENERATOR": str(viewStateGenerator),
                "__EVENTVALIDATION": str(eventValidation),
                "Email": str(self.email),
                "Password": str(self.password),
                "Remember": "on",
                "Email2": "",
                "_ASYCNPOST": True,
                "BtnSubmit": "Login",
            }

            s.post(loginURL, data=requestData, headers=newHeaders)

            cookies = s.cookies.get_dict()
            expire = {}
            for cookie in s.cookies:
                if cookie.name == "Email":
                    emailExpires = cookie.expires  # ?Todo: Convert from epoch to datetime
                    expire["Email"] = emailExpires
                if cookie.name == "TCRAuth":
                    TCRAuthExpires = cookie.expires  # ?Todo: Convert from epoch to datetime
                    expire["TCRAuth"] = TCRAuthExpires

        return cookies, expire

    def login(self):
        getCookie = self.getCookies()
        print("Logged Into TCR as: {}".format(self.email))
        self.setCookie(getCookie[0])
        self.setCookieExpiration(getCookie[1])
        self.setHeaders(getCookie[0])
