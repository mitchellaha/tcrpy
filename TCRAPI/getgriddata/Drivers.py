from TCRAPI.models import ConditionsModel, FilterModel

class driversClass:
    def __init__(self):
        self.gridID = 34
        self.gridName = "DRIVERS"
        self.filterConditions = FilterModel(
            Conditions=[
                ConditionsModel(
                    Attribute="Status",
                    Values=["A"],
                    Operator=12
                ),
            ]
        )
