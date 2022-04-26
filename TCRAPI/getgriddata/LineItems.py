from TCRAPI.models import ConditionsModel, FilterModel


class lineItemsClass:
    def __init__(self):
        self.gridID = 30
        self.gridName = "LINEITEMS"
        self.filterConditions = FilterModel(
            Conditions=[
                ConditionsModel(
                    Attribute="Status",
                    Values=["A"],
                    Operator=12
                ),
            ]
        )
