from TCRAPI.models import ConditionsModel, FilterModel


class ticketItemsClass:
    GRIDID = 47
    GRIDNAME = "TICKETITEMS"
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
