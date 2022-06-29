
from TCRAPI.models import ConditionsModel, FilterModel


class invoiceDetailsClass:
    GRIDID = 143
    GRIDNAME = "INVOICEDETAILS"
    def __init__(self, InvoiceID):
        self.InvoiceID = InvoiceID
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
