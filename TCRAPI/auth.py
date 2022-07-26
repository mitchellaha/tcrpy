import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup


class auth:
    loginURL = "http://apps.tcrsoftware.com/tcr_2/login.aspx"
    def __init__(self, email=None, password=None):
        load_dotenv()
        self.email = email or os.getenv("email")
        self.password = password or os.getenv("password")
        self.header = None
        self.cookies = None
        self.expire = None
        self.set_header()


    def get_cookies(self):
        """
        Returns TCR cookies[0] and expiration[1]
        """
        with requests.Session() as s:
            s.headers.update(
                {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
            )
            loginPageContent = s.get(self.loginURL)
            soup = BeautifulSoup(loginPageContent.content, 'html.parser') # Rip the form data from the page with BS4.

            loginPostHeaders = {
                "X-MicrosoftAjax": "Delta=true",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://apps.tcrsoftware.com/tcr_2/login.aspx"
            }

            loginData = {
                "ScriptManager1": "UpdatePanel1|BtnSubmit",
                "__LASTFOCUS": "",
                "__EVENTTARGET": "",
                "__EVENTARGUMENT": "",
                "__VIEWSTATE": str(soup.select_one("#__VIEWSTATE")["value"]),
                "__VIEWSTATEGENERATOR": str(soup.select_one("#__VIEWSTATEGENERATOR")["value"]),
                "__EVENTVALIDATION": str(soup.select_one("#__EVENTVALIDATION")["value"]),
                "Email": str(self.email),
                "Password": str(self.password),
                "Remember": "on",
                "Email2": "",
                "_ASYCNPOST": True,
                "BtnSubmit": "Login",
            }

            s.post(self.loginURL, data=loginData, headers=loginPostHeaders)

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


    def set_header(self):
        cookies, expire = self.get_cookies()
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
