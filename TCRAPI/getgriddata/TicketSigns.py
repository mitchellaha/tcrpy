from TCRAPI.models import ConditionsModel, FilterModel


class ticketSignsClass:
    def __init__(self, TicketID):
        self.TicketID = TicketID
        self.gridID = 15
        self.gridName = "TSIGN"
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
