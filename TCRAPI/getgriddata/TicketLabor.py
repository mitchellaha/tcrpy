from TCRAPI.models import ConditionsModel, FilterModel

class ticketLaborClass:
    def __init__(self, TicketID):
        self.TicketID = TicketID
        self.gridID = 16
        self.gridName = "TLABOR"
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
