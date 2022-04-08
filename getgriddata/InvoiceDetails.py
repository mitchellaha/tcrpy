from tcr_interactions.get_grid import getGridDataFields
from tcr_interactions.get_user_settings import getGridSortSettings
from tcr_interactions.post_models import ConditionsModel, FilterModel


class invoiceDetailsClass:
    def __init__(self, InvoiceID):
        self.InvoiceID = InvoiceID
        self.gridID = 143
        self.gridName = "INVOICEDETAILS"
        self.Attributes = getGridDataFields(self.gridID)
        self.gridCustomSort = getGridSortSettings(self.gridID)
        self.filterConditions = FilterModel(
            Conditions=[
                ConditionsModel(
                    Attribute="invoiceID",
                    Values=[
                        str(self.InvoiceID)
                    ],
                    Operator=1
                )
            ]
        )
