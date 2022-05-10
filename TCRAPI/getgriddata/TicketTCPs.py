from TCRAPI.models import ConditionsModel, FilterModel

class ticketTCPsClass:
    def __init__(self, TicketID):
        self.TicketID = TicketID
        self.gridID = 126
        self.gridName = "TICKETTCPS"
        self.AttachmentURL = "https://apps.tcrsoftware.com/tcr_2/webforms/edit.aspx?id=JTCP&download=1&TCPID="
        self.filterConditions = FilterModel(
            Conditions=[
                ConditionsModel(
                    Attribute="TicketID",
                    Values=[
                        str(self.TicketID)
                    ],
                    Operator=1
                )
            ]
        )