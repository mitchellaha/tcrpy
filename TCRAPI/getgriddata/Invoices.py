from TCRAPI.models import FilterModel

class invoicesClass:
    def __init__(self):
        self.gridID = 20
        self.gridName = "INVOICES"
        self.filterConditions = FilterModel(
            Conditions=[]
        )
