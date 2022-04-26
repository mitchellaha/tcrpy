from TCRAPI.models import ConditionsModel, FilterModel


class ticketItemsClass:
    def __init__(self, TicketID):
        self.TicketID = TicketID
        self.gridID = 47
        self.gridName = "TICKETITEMS"
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
