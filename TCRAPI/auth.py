import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup


class auth:
    def __init__(self, email=None, password=None):
        load_dotenv()

        self.email = email
        if email is None:
            self.email = os.getenv("email")

        self.password = password
        if password is None:
            self.password = os.getenv("password")

        # self.getHeaders = self.headers()
        self.header = self.headers()
        self.cookies = None
        self.expire = None


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


    def headers(self):
        cookies, expire = self.getCookies()
        headers = {
            'DNT': '1',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json'
        }
        cookie = "Email={}; ASP.NET_SessionId={}; TCRAuth={}".format(
            cookies["Email"], cookies["ASP.NET_SessionId"], cookies["TCRAuth"])
        headers["Cookie"] = cookie
        self.header = headers
        self.cookies = cookies
        self.expire = expire
        return headers
