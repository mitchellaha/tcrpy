from TCRAPI.models import ConditionsModel, FilterModel


class customerContactsClass:
    def __init__(self, CustomerID):
        self.CustomerID = CustomerID
        self.gridID = 139
        self.gridName = "CONTACTS"
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
