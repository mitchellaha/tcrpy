from TCRAPI.models import FilterModel

class invoicesClass:
    GRIDID = 20
    GRIDNAME = "INVOICES"
    def __init__(self):
        self.filterConditions = FilterModel(
            Conditions=[]
        )
