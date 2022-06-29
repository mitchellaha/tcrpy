from TCRAPI.models import ConditionsModel, FilterModel


class ticketSignsClass:
    GRIDID = 15
    GRIDNAME = "TSIGN"
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
