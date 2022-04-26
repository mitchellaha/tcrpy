from TCRAPI.models import ConditionsModel, FilterModel


class customerJobsClass:
    def __init__(self, CustomerID):
        self.CustomerID = CustomerID
        self.gridID = 2
        self.gridName = "CJOBS"
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
