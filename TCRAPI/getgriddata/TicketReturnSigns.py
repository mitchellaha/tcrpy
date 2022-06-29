from TCRAPI.models import ConditionsModel, FilterModel


class ticketReturnSignsClass:
    GRIDID = 48
    GRIDNAME = "TRETURNSIGNS"
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
