from TCRAPI.models import ConditionsModel, FilterModel


class customerContactsClass:
    GRIDID = 139
    GRIDNAME = "CONTACTS"
    def __init__(self, CustomerID):
        self.CustomerID = CustomerID
        self.filterConditions = FilterModel(
            Conditions=[
                ConditionsModel(
                    Attribute="EntityID",
                    Values=[
                        "1"
                    ],
                    Operator=1
                ),
                ConditionsModel(
                    Attribute="RelatedRecordID",
                    Values=[
                        str(self.CustomerID)
                    ],
                    Operator=1
                )
            ]
        )
