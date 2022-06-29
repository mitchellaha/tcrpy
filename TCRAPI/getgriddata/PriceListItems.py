from TCRAPI.models import ConditionsModel, FilterModel

class priceListItemsClass:
    GRIDID = 42
    GRIDNAME = "PRICELISTITEMS"
    def __init__(self, PriceListID):
        self.PriceListID = PriceListID
        self.filterConditions = FilterModel(
            Conditions=[
                ConditionsModel(
                    Attribute="PriceListID",
                    Values=[str(PriceListID)],
                    Operator=12
                ),
            ]
        )
