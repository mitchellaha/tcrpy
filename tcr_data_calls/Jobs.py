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
            Conditions=[
                ConditionsModel(
                    Attribute="Status",
                    Values=["O", "P", "C", "I", "X"],
                    Operator=12
                ),
            ]
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
            Conditions=[self.filterConditions.Conditions[0]],
            Filter=FilterSearchConditionsModel(
                Conditions=Conditions,
                GroupOperator=2
            )
        )
        return respond

    def setStatusFilter(self, Status):
        """
        Sets the status filter for the customers grid.
            - O - Open
            - P - Pending
            - C - Closed
            - I - Invoiced
            - X - Canceled
        """
        if isinstance(Status, list):
            self.filterConditions.Conditions = [
                ConditionsModel(
                    Attribute="Status",
                    Values=Status,
                    Operator=12
                ),
            ]
        if isinstance(Status, str):
            self.filterConditions.Conditions = [
                ConditionsModel(
                    Attribute="Status",
                    Values=[Status],
                    Operator=12
                ),
            ]
