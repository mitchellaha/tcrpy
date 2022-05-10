from TCRAPI.models import FilterModel

class priceListsClass:
    def __init__(self):
        self.gridID = 29
        self.gridName = "PRICELIST"
        self.filterConditions = FilterModel(
            Conditions=[]
        )