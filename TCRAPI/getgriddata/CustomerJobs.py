from TCRAPI.models import ConditionsModel, FilterModel


class customerJobsClass:
    GRIDID = 2
    GRIDNAME = "CJOBS"
    def __init__(self, CustomerID):
        self.CustomerID = CustomerID
        self.filterConditions = FilterModel(
            Conditions=[
                ConditionsModel(
                    Attribute="CustomerID",
                    Values=[
                        str(self.CustomerID)
                    ],
                    Operator=1
                )
            ]
        )
