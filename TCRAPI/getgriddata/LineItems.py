from TCRAPI.models import ConditionsModel, FilterModel


class lineItemsClass:
    GRIDID = 30
    GRIDNAME = "LINEITEMS"
    def __init__(self):
        self.filterConditions = FilterModel(
            Conditions=[
                ConditionsModel(
                    Attribute="Status",
                    Values=["A"],
                    Operator=12
                ),
            ]
        )
