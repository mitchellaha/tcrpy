from TCRAPI.models import ConditionsModel, FilterModel


class jobTicketsClass:
    def __init__(self, JobID):
        self.JobID = JobID
        self.gridID = 10
        self.gridName = "JTICKETS"
        self.filterConditions = FilterModel(
            Conditions=[
                ConditionsModel(
                    Attribute="JobID",
                    Values=[
                        str(self.JobID)
                    ],
                    Operator=1
                )
            ]
        )
