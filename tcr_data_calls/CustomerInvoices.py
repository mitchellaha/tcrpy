from tcr_interactions.get_user_settings import getGridSortSettings
from tcr_interactions.get_grid import getGridDataFields
from tcr_interactions.post_models import FilterModel, ConditionsModel

class customerInvoicesClass:
    def __init__(self, CustomerID):
        self.CustomerID = CustomerID
        self.gridID = 5
        self.gridName = "CINVOICES"
        self.Attributes = getGridDataFields(self.gridID)
        self.gridCustomSort = getGridSortSettings(self.gridID)
        self.filterConditions = FilterModel(
            Conditions=[
                ConditionsModel(
                    Attribute="CustomerID",
                    Values=[
                        str(self.CustomerID)
                    ],
                    Operator=1
                )
            ]
        )
