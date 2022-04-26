
from TCRAPI.models import ConditionsModel, FilterModel


class jobInvoicesClass:
    def __init__(self, JobID):
        self.JobID = JobID
        self.gridID = 11
        self.gridName = "JINVOICES"
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
