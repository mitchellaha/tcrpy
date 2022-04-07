from tcr_interactions.get_grid import getGridDataFields, getGridQuickSearchFields
from tcr_interactions.get_user_settings import getGridSortSettings
from tcr_interactions.post_models import ConditionsModel, FilterModel, FilterSearchConditionsModel, FilterSearchModel


# ? Status: A-Active, P-Pre-Pay, H-On Hold, I-Inactive
class customersClass:
    def __init__(self):
        self.gridID = 1
        self.gridName = "CUSTOMERS"
        self.Attributes = getGridDataFields(self.gridID)
        self.gridCustomSort = getGridSortSettings(self.gridID)
        self.filterConditions = FilterModel(
            Conditions=[
                ConditionsModel(
                    Attribute="Status",
                    Values=["A", "P", "H", "I"],
                    Operator=12
                ),
            ]
        )

    def search(self, SearchQuery):
        AttributeList = getGridQuickSearchFields(self.gridID)
        Conditions = []
        for Attribute in AttributeList:
            Conditions.append(
                ConditionsModel(
                    Attribute=Attribute,
                    Values=[
                        SearchQuery
                    ],
                    Operator=10
                )
            )
        respond = FilterSearchModel(
            Conditions=[self.filterConditions.Conditions[0]],
            Filter=FilterSearchConditionsModel(
                Conditions=Conditions,
                GroupOperator=2
            )
        )
        return respond

    def setStatusFilter(self, Status):
        """
        Sets the status filter for the customers grid.
            - A - Active
            - P - Pre-Pay
            - H - On Hold
            - I - Inactive
        """
        if isinstance(Status, list):
            self.filterConditions.Conditions = [
                ConditionsModel(
                    Attribute="Status",
                    Values=Status,
                    Operator=12
                ),
            ]
        if isinstance(Status, str):
            self.filterConditions.Conditions = [
                ConditionsModel(
                    Attribute="Status",
                    Values=[Status],
                    Operator=12
                ),
            ]
