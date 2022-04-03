from tcr_interactions.get_grid import getGridDataFields
from tcr_interactions.get_user_settings import getGridSortSettings
from tcr_interactions.post_models import ConditionsModel, FilterModel, FilterSearchConditionsModel, FilterSearchModel

class jobsClass:
    def __init__(self):
        self.gridID = 8
        self.gridName = "JOBS"
        self.Attributes = getGridDataFields(self.gridID)
        self.gridCustomSort = getGridSortSettings(self.gridID)
        self.filterConditions = FilterModel(
            Conditions=[]
        )

    def search(self, SearchQuery):
        AttributeList = [
            "CustomerName",
            "BranchName",
            "JobNumber",
            "JobReferenceNumber",
            "JobType",
            "Name",
            "JobAddress1",
            "City",
            "State",
            "CustomerJobNumber",
            "PONumber",
            "ForemanName",
            "ForemanPhone"
        ]
        Conditions = []
        for Attribute in AttributeList:
            Conditions.append(
                ConditionsModel(
                    Attribute=Attribute,
                    Values=[
                        SearchQuery
                    ],
                    Operator=10
                )
            )
        respond = FilterSearchModel(
            Conditions=[],
            Filter=FilterSearchConditionsModel(
                Conditions=Conditions,
                GroupOperator=2
            )
        )
        return respond
