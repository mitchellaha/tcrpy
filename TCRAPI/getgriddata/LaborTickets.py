from TCRAPI.models import FilterModel


class laborTicketClass:
    def __init__(self):
        self.gridID = 52
        self.gridName = "LABORTICKETS"
        self.filterConditions = FilterModel(
            Conditions=[]
        )
