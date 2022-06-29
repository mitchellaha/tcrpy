from TCRAPI.models import ConditionsModel, FilterModel


class jobsClass:
    GRIDID = 8
    GRIDNAME = "JOBS"
    def __init__(self):
        self.filterConditions = FilterModel(
            Conditions=[
                ConditionsModel(
                    Attribute="Status",
                    Values=["O", "P", "C", "I", "X"],
                    Operator=12
                ),
            ]
        )

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
