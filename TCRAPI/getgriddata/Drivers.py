from TCRAPI.models import ConditionsModel, FilterModel

class driversClass:
    GRIDID = 34
    GRIDNAME = "DRIVERS"
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
