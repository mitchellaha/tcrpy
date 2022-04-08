from tcr_interactions.get_grid import getGridDataFields
from tcr_interactions.get_user_settings import getGridSortSettings
from tcr_interactions.post_models import ConditionsModel, FilterModel


class ticketReturnSignsClass:
    def __init__(self, TicketID):
        self.TicketID = TicketID
        self.gridID = 48
        self.gridName = "TRETURNSIGNS"
        self.Attributes = getGridDataFields(self.gridID)
        self.gridCustomSort = getGridSortSettings(self.gridID)
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
