from TCRAPI.models import ConditionsModel, FilterModel

class ticketLaborClass:
    GRIDID = 16
    GRIDNAME = "TLABOR"
    def __init__(self, TicketID):
        self.TicketID = TicketID
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
