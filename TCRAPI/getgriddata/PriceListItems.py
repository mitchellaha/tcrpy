from TCRAPI.models import ConditionsModel, FilterModel

class priceListItemsClass:
    def __init__(self, PriceListID):
        self.PriceListID = PriceListID
        self.gridID = 42
        self.gridName = "PRICELISTITEMS"
        self.filterConditions = FilterModel(
            Conditions=[
                ConditionsModel(
                    Attribute="PriceListID",
                    Values=[str(PriceListID)],
                    Operator=12
                ),
            ]
        )
