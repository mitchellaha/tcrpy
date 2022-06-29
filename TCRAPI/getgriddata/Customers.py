from TCRAPI.models import ConditionsModel, FilterModel


# ? Status: A-Active, P-Pre-Pay, H-On Hold, I-Inactive
class customersClass:
    GRIDID = 1
    GRIDNAME = "CUSTOMERS"
    def __init__(self):
        self.filterConditions = FilterModel(
            Conditions=[
                ConditionsModel(
                    Attribute="Status",
                    Values=["A", "P", "H", "I"],
                    Operator=12
                ),
            ]
        )

    def setStatusFilter(self, Status):
        """
        Sets the status filter for the customers grid.
            - A - Active
            - P - Pre-Pay
            - H - On Hold
            - I - Inactive
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
