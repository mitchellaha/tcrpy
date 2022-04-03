from GetGridData import *
# from .tcr_interactions.post_models import *
import requests
import json
from common import gridDataUrl, headers

class tItemsOBJ:
    GridID = 47
    Attributes = [
        "TicketItemID",
        "TicketID",
        "ItemCode",
        "Description",
        "RateTypeName",
        "SubItemDescription",
        "QuanityOnHand",
        "QuantityNeeded",
        "QuantityReturned",
        "PrintOnInvoice",
        "PrintOnTicket",
    ]

    def payload(self, ticketID, startIndex=1, recordCount=100):
        TicketItems = Root(
            query=Query(
                GridID=self.GridID,
                RecordCount=recordCount,
                Filter=Filter(
                    Conditions=[
                        Conditions(
                            Attribute="TicketID",
                            Values=[
                                str(ticketID)
                            ],
                            Operator=QueryParamOperator["Equal"]
                        )
                    ]
                ),
                StartIndex=startIndex,
                Attributes=self.Attributes,
                Sort=[
                    Sort(
                        Attribute="ItemCode",
                        Order=QuerySort["ASC"]
                    )
                ],
                CustomSort=None,
            )
        ).json()
        return TicketItems

    def getTicketItems(self, ticketID, startIndex=1, recordCount=100):
        TicketItems = self.payload(ticketID, startIndex, recordCount)
        response = requests.post(gridDataUrl, headers=headers, data=TicketItems).json()
        # resultjson = response.json()
        resultjson = json.loads(response["d"]["Result"])
        # print(resultjson)
        count = resultjson["RecordCount"]
        data = resultjson["Data"]
        return count, data
