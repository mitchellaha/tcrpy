from TCRAPI.models import ConditionsModel, FilterModel


class ticketReturnSignsClass:
    def __init__(self, TicketID):
        self.TicketID = TicketID
        self.gridID = 48
        self.gridName = "TRETURNSIGNS"
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
