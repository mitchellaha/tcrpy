from TCRAPI.models import ConditionsModel, FilterModel


class jobTicketsClass:
    GRIDID = 10
    GRIDNAME = "JTICKETS"
    def __init__(self, JobID):
        self.JobID = JobID
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
