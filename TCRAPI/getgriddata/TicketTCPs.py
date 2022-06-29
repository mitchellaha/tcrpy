from TCRAPI.models import ConditionsModel, FilterModel

class ticketTCPsClass:
    GRIDID = 126
    GRIDNAME = "TICKETTCPS"
    def __init__(self, TicketID):
        self.TicketID = TicketID
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