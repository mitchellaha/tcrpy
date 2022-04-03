from tcr_interactions.get_grid import getGridDataFields
from tcr_interactions.get_user_settings import getGridSortSettings
from tcr_interactions.post_models import ConditionsModel, FilterModel


class customerContactsClass:
    def __init__(self, CustomerID):
        self.CustomerID = CustomerID
        self.gridID = 139
        self.gridName = "CONTACTS"
        self.Attributes = getGridDataFields(self.gridID)
        self.gridCustomSort = getGridSortSettings(self.gridID)
        self.filterConditions = FilterModel(
            Conditions=[
                ConditionsModel(
                    Attribute="EntityID",
                    Values=[
                        "1"
                    ],
                    Operator=1
                ),
                ConditionsModel(
                    Attribute="RelatedRecordID",
                    Values=[
                        str(self.CustomerID)
                    ],
                    Operator=1
                )
            ]
        )
