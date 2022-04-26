from TCRAPI.models import ConditionsModel, FilterModel


class driverScheduleClass:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.gridID = 54
        self.gridName = "DRIVERSCHEDULE"
        self.filterConditions = FilterModel(
            Conditions=[
                ConditionsModel(
                    Attribute="StartDate",
                    Values=[
                        str(self.start)
                    ],
                    Operator=6
                ),
                ConditionsModel(
                    Attribute="EndDate",
                    Values=[
                        str(self.end)
                    ],
                    Operator=6
                ),
                ConditionsModel(
                    Attribute="BranchID",
                    Values=[
                        ""
                    ],
                    Operator=1
                ),
                ConditionsModel(
                    Attribute="Status",
                    Values=[
                        ""
                    ],
                    Operator=1
                ),
                ConditionsModel(
                    Attribute="TransactionID",
                    Values=[
                        ""
                    ],
                    Operator=1
                ),
                ConditionsModel(
                    Attribute="RecordType",
                    Values=[
                        1
                    ],
                    Operator=1
                )
            ]
        )
