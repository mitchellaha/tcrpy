
from TCRAPI.models import ConditionsModel, FilterModel


class jobInvoicesClass:
    GRIDID = 11
    GRIDNAME = "JINVOICES"
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
