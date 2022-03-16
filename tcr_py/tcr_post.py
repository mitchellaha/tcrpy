from .common import *


entityRecord = "http://apps.tcrsoftware.com/tcr_2/webservices/CustomEntity.asmx/GetEntityRecord"
auditData = "http://apps.tcrsoftware.com/tcr_2/webservices/Audit.asmx/GetAuditData"
gridData = "http://apps.tcrsoftware.com/tcr_2/webservices/data.asmx/GetGridData"
ticketCount = "https://apps.tcrsoftware.com/tcr_2/webservices/DashboardService.asmx/GetTicketsCount"
getGridID = "http://apps.tcrsoftware.com/tcr_2/webservices/config.asmx/GetGridByID"

class tcrPost:
    """
    class tcrPost:
        performs a post request to TCR in replace of requests.post and headers and URls
    method:
        data = {*GRID PAYLOAD HERE*}
        send = tcrPost(
            payload = data,
            type = tcrPost.getGridData,
        ).request()
    If:
        .request(parseD=True): will return everything within TCRs d json key
        .request(parseD=False): will return the entire json response inside of the TCR d json key
    """
    def __init__(self, payload=None, tcrurl=None):
        self.payload = payload
        self.tcrurl = tcrurl
        self.headers = {
            'DNT': '1',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'Content-Type': 'application/json; charset=utf-8',
            'Accept': 'application/json',
            'Cookie': str(os.getenv('token'))}

    def request(self):
        payload = json.dumps(self.payload)
        response = requests.post(self.tcrurl, headers=self.headers, data=payload)
        return json.loads(response.text)
