from TCRAPI.models import ConditionsModel, FilterModel, Filter


class ticketsClass:
    GRIDID = 9
    GRIDNAME = "TICKETS"
    # filterConditions = Filter()
    # filterConditions.AddCondition("Status", ["A", "E", "F", "I", "V"], 12)
    def __init__(self):
        self.filterConditions = Filter()
        self.filterConditions.add_condition("Status", ["A", "E", "F", "I", "V"], 12)
