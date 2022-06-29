from TCRAPI.models import FilterModel


class laborTicketClass:
    GRIDID = 52
    GRIDNAME = "LABORTICKETS"
    def __init__(self):
        self.filterConditions = FilterModel(
            Conditions=[]
        )
