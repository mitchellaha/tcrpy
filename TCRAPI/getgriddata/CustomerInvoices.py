from TCRAPI.models import ConditionsModel, FilterModel


class customerInvoicesClass:
    GRIDID = 5
    GRIDNAME = "CINVOICES"
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
