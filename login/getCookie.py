from turtle import setheading
from bs4 import BeautifulSoup
import requests
import json

def getTCRAuth(email, password):
    """
    Returns a Dictionary Of Cookies Needed For Login To TCR
    input: email, password
    output: dictionary of cookies, expirey date
    [0] = dictionary of cookies
    [1] = expirey date
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
        viewStateGenerator = soup.select_one("#__VIEWSTATEGENERATOR")["value"]
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
            "Email": str(email),
            "Password": str(password),
            "Remember": "on",
            "Email2": "",
            "_ASYCNPOST": True,
            "BtnSubmit": "Login",
        }

        s.post("http://apps.tcrsoftware.com/tcr_2/login.aspx", data=requestData, headers=newHeaders)

        cookies = s.cookies.get_dict()
        expire = {}
        for cookie in s.cookies:
            if cookie.name == "Email":
                emailExpires = cookie.expires  # ! RETURNS EPOCH TIME
                expire["Email"] = emailExpires
                # print("Email Expires: " + str(emailExpires))
            if cookie.name == "TCRAuth":
                TCRAuthExpires = cookie.expires  # ! RETURNS EPOCH TIME
                # print("TCRAuth Expires: " + str(TCRAuthExpires))
                expire["TCRAuth"] = TCRAuthExpires

        # if __name__ == "__main__":  # ? Not Needed But Didnt Want To Remove Yet (For Testing)
        #     cookies_dictionary = page.cookies.get_dict()
        #     sessionID = cookies_dictionary["ASP.NET_SessionId"]
        #     print("Session ID: " + str(sessionID))
        #     print("")
        #     print("Cookies: " + str(cookies))
        #     print("")

    return cookies, expire


def appendHeader(cookieDict):
    """
    Appends the Cookies to the Headers
    """
    headers = {
        'DNT': '1',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Content-Type': 'application/json; charset=utf-8',
        'Accept': 'application/json'
    }
    cookie = "Email={}; ASP.NET_SessionId={}; TCRAuth={}".format(cookieDict["Email"], cookieDict["ASP.NET_SessionId"], cookieDict["TCRAuth"])
    headers["Cookie"] = cookie
    return headers


def cookieCheck(cookieDict):
    """
    Checks to See if the Saved Cookies Work Still
    """

    headers = appendHeader(cookieDict)
    data = {
        "includeBilling": True
    }
    response = requests.post("http://apps.tcrsoftware.com/tcr_2/webservices/DashboardService.asmx/GetCompanyOverview", headers=headers, json=data)
    if response.status_code == 200:
        print("Cookies Work")
        return True
    if response.status_code == 401:
        print("Cookies Do Not Work")
        return False


def saveCookies(cookies):
    """
    Saves The Cookies Dictionary To A File Named cookies.json
    """
    with open('./login/cookies.json', 'w') as f:
        json.dump(cookies, f)


def setHeaders(cookieDict, email, password):
    """
    Returns the Headers Needed To Make A Request To TCR including the cookies.
    input: Cookie Dictionary
    output: Dictionary of Headers
    """
    cookieTest = cookieCheck(cookieDict)  # ? Check to see if the cookies are still valid

    headers = {
        'DNT': '1',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Content-Type': 'application/json; charset=utf-8',
        'Accept': 'application/json'
    }

    if cookieTest is False:  # ? If the cookies are no longer valid, get new ones
        login = getTCRAuth(email, password)[0]
        saveCookies(login)
        headers = appendHeader(login)
        # headers["Cookie"] = cookie
        return headers
    if cookieTest is True:  # ? If the cookies are still valid, use them
        headers = appendHeader(cookieDict)
        # headers["Cookie"] = cookie
        return headers



if __name__ == "__main__":
    from dotenv import load_dotenv
    import os
    load_dotenv()

    email = os.getenv("email")
    password = os.getenv("password")
    
    # x = getTCRAuth(email, password)
    # saveCookies(x[0])
    # print(x[0])


    with open("login/cookies.json") as f:
        savedCookies = json.load(f)
    # cookieCheck(savedCookies)
    print(setHeaders(savedCookies, email, password))

    # cookieCheck()
