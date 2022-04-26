
from TCRAPI.models import ConditionsModel, FilterModel


class invoiceDetailsClass:
    def __init__(self, InvoiceID):
        self.InvoiceID = InvoiceID
        self.gridID = 143
        self.gridName = "INVOICEDETAILS"
        self.filterConditions = FilterModel(
            Conditions=[
                ConditionsModel(
                    Attribute="invoiceID",
                    Values=[
                        str(self.InvoiceID)
                    ],
                    Operator=1
                )
            ]
        )
