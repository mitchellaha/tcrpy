from tcr_interactions.get_grid import getGridDataFields
from tcr_interactions.get_user_settings import getGridSortSettings
from tcr_interactions.post_models import ConditionsModel, FilterModel, FilterSearchConditionsModel, FilterSearchModel


class customersClass:
    def __init__(self):
        self.gridID = 1
        self.gridName = "CUSTOMERS"
        self.Attributes = getGridDataFields(self.gridID)
        self.gridCustomSort = getGridSortSettings(self.gridID)
        self.filterConditions = FilterModel(
            Conditions=[]
        )

    def searchCustomers(self, SearchQuery):
        AttributeList = [
            "CustomerCode",
            "CustomerName",
            "Address1",
            "City",
            "ZipCode",
            "Contact",
            "SalespersonName",
            "PriceListDescription",
        ]
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
            Conditions=[],
            Filter=FilterSearchConditionsModel(
                Conditions=Conditions,
                GroupOperator=2
            )
        )
        return respond
