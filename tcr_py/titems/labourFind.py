# NEED TO PUT ITEM LIST IN SOMEWHERE
"""
Class labourfind:
    Returns a Dictionary of Item Labour With Their Respective Counts.

"""
class labourFind:
    def __init__(self, ticketID):
        self.ticketID = ticketID
    
    def iList(self):
        iList = itemList(self.ticketID)  # type: ignore # noqa F821
        data = iList["Data"]
        return data

    def flaggers(self):
        flagDict = {
            "Flagger": 0,
            "Flagger_OT": 0,
            "Flagger_Cert": 0,
            "Flagger_Sun": 0
        }
        for ticket in self.iList():
            quantity = ticket["QuantityRequested"]
            if ticket["ItemCode"] == "FLAGGING21":
                flagDict["Flagger"] += int(quantity)
            if ticket["ItemCode"] == "FLAGOT21":
                flagDict["Flagger_OT"] += int(quantity)
            if ticket["ItemCode"] == "FLAGCERT21":
                flagDict["Flagger_Cert"] += int(quantity)
            if ticket["ItemCode"] == "FLAGSUN21":
                flagDict["Flagger_Sun"] += int(quantity)
        return flagDict
    
    def labour(self):
        labourDict = {
            "Labour": 0,
            "Labour_OT": 0,
            "Labour_Cert": 0,
            "Labour_Sun": 0
        }
        for ticket in self.iList():
            quantity = ticket["QuantityRequested"]
            if ticket["ItemCode"] == "LABORER21":
                labourDict["Labour"] += int(quantity)
            if ticket["ItemCode"] == "LAB/OT21":
                labourDict["Labour_OT"] += int(quantity)
            if ticket["ItemCode"] == "CERTLABOR":
                labourDict["Labour_Cert"] += int(quantity)
            if ticket["ItemCode"] == "LAB/SUN21":
                labourDict["Labour_Sun"] += int(quantity)
        return labourDict

    def utc(self):
        UTCDict = {
            "UTC": 0,
            "UTC_Denver": 0,
            "UTC_TMA": 0,
        }
        for ticket in self.iList():
            quantity = ticket["QuantityRequested"]
            if ticket["ItemCode"] == "UTC":
                UTCDict["UTC"] += int(quantity)
            if ticket["ItemCode"] == "CCD UTC":
                UTCDict["UTC_Denver"] += int(quantity)
            if ticket["ItemCode"] == "UTC/ATTEN":
                UTCDict["UTC_TMA"] += int(quantity)
        return UTCDict
    
    def tcs(self):
        TCSDict = {
            "TCS": 0,
            "TCS_OT": 0,
            "TCS_Sun": 0
        }
        for ticket in self.iList():
            quantity = ticket["QuantityRequested"]
            if ticket["ItemCode"] == "TCS/TRK":
                TCSDict["TCS"] += int(quantity)
            if ticket["ItemCode"] == "TCS/OT":
                TCSDict["TCS_OT"] += int(quantity)
            if ticket["ItemCode"] == "TCS/SUN":
                TCSDict["TCS_Sun"] += int(quantity)
        return TCSDict

    def other(self):
        OTHERDict = {
            "TMA_Driver": 0,
            "AFAD": 0,
            "AFAD_OT": 0,
            "Freight_Forklift": 0
        }
        for ticket in self.iList():
            quantity = ticket["QuantityRequested"]
            if ticket["ItemCode"] == "ATTENTRKDR":
                OTHERDict["TMA_Driver"] += int(quantity)
            if ticket["ItemCode"] == "AFAD Oper":
                OTHERDict["AFAD"] += int(quantity)
            if ticket["ItemCode"] == "AFAD":
                OTHERDict["AFAD_OT"] += int(quantity)
            if ticket["ItemCode"] == "FREIGHT":
                OTHERDict["Freight_Forklift"] += int(quantity)
        return OTHERDict

    def certified(self):
        if self.flaggers()["Flagger_Cert"] > 0:
            return True
        if self.labour()["Labour_Cert"] > 0:
            return True
        else:
            return False

    def total(self):
        total = {}
        total.update(self.flaggers())
        total.update(self.labour())
        total.update(self.utc())
        total.update(self.tcs())
        total.update(self.other())
        return total
