from tcr_interactions.get_grid import getGridDataFields
from tcr_interactions.get_user_settings import getGridSortSettings
from tcr_interactions.post_models import ConditionsModel, FilterModel


class jobTicketsClass:
    def __init__(self, JobID):
        self.JobID = JobID
        self.gridID = 10
        self.gridName = "JTICKETS"
        self.Attributes = getGridDataFields(self.gridID)
        self.gridCustomSort = getGridSortSettings(self.gridID)
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
