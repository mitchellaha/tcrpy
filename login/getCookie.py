from bs4 import BeautifulSoup
import requests
import json

def getTCRAuth(email, password):
    """
    Returns a Dictionary Of Cookies Needed For Login To TCR
    input: email, password
    output: dictionary of cookies, expirey date
    """
    with requests.Session() as s:
        loginURL = "http://apps.tcrsoftware.com/tcr_2/login.aspx"

        s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})
        page = s.get(loginURL)

        cookies_dictionary = page.cookies.get_dict()
        sessionID = cookies_dictionary["ASP.NET_SessionId"]

        print("Session ID: " + str(sessionID))

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
        print("")
        print("Cookies: " + str(cookies))
        print("")

        expire = {}
        for cookie in s.cookies:
            if cookie.name == "Email":
                emailExpires = cookie.expires  # ! RETURNS EPOCH TIME
                expire["Email"] = emailExpires
                print("Email Expires: " + str(emailExpires))
            if cookie.name == "TCRAuth":
                TCRAuthExpires = cookie.expires  # ! RETURNS EPOCH TIME
                print("TCRAuth Expires: " + str(TCRAuthExpires))
                expire["TCRAuth"] = TCRAuthExpires

    return cookies, expire

def saveCookies(cookies):
    """
    Saves The Cookies Dictionary To A File Named cookies.json
    """
    with open('./login/cookies.json', 'w') as f:
        json.dump(cookies, f)

def setHeaders(cookieDict):
    """
    Returns the Headers Needed To Make A Request To TCR including the cookies.
    input: Cookie Dictionary
    output: Dictionary of Headers
    """
    appURL = "http://apps.tcrsoftware.com/tcr_2/default.aspx"

    headers = {
        'DNT': '1',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'Content-Type': 'application/json; charset=utf-8',
        'Accept': 'application/json'
    }

    loginTest = requests.get(appURL, cookies=cookieDict)

    if loginTest.status_code == 302:
        login = getTCRAuth()[0]
        cookie = "Email={}; ASP.NET_SessionId={}; TCRAuth={}".format(login["Email"], login["ASP.NET_SessionId"], login["TCRAuth"])
        headers["Cookie"] = cookie
        return headers
    if loginTest.status_code == 200:
        cookie = "Email={}; ASP.NET_SessionId={}; TCRAuth={}".format(cookieDict["Email"], cookieDict["ASP.NET_SessionId"], cookieDict["TCRAuth"])
        headers["Cookie"] = cookie
        return headers
    else:
        print("Login Error: " + str(loginTest.status_code))
        return False


if __name__ == "__main__":
    from dotenv import load_dotenv
    import os
    load_dotenv()

    email = os.getenv("email")
    password = os.getenv("password")
    
    x = getTCRAuth(email, password)
    saveCookies(x[0])
    print(x[0])
