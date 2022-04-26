from TCRAPI.models import ConditionsModel, FilterModel


class customerInvoicesClass:
    def __init__(self, CustomerID):
        self.CustomerID = CustomerID
        self.gridID = 5
        self.gridName = "CINVOICES"
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
