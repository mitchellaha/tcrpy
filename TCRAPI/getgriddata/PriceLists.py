from TCRAPI.models import FilterModel

class priceListsClass:
    GRIDID = 29
    GRIDNAME = "PRICELIST"
    def __init__(self):
        self.filterConditions = FilterModel(
            Conditions=[]
        )