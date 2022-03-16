from .tcr_post import *
from .common import *

class gridCondition:
    """
    Returns Grid Condition Filter Format
    gridCondition("StartDate", 6, vList= ["01/01/2100"])
    or
    gridCondition("StartDate", 4, v1="01/01/2100", v2="01/02/2100", v3="01/03/2100")
    """
    def __init__(self, attribute: str, operator: int, **kwargs):
        self.attribute = attribute
        self.operator = operator
        self.v1 = kwargs.get('v1')
        self.v2 = kwargs.get('v2')
        self.v3 = kwargs.get('v3')
        self.vList = kwargs.get('vList')
    
    def dict(self):
        if self.v3 is not None:
            opVal = [self.v1, self.v2, self.v3]
        elif self.v2 is not None:
            opVal = [self.v1, self.v2]
        elif self.v1 is not None:
            opVal = [self.v1]
        elif self.vList is not None:
            opVal = self.vList
        else:
            opVal = [""]
        return {
            "Attribute": self.attribute,
            "Operator": self.operator,
            "Values": opVal
        }

    def list(self):
        return [self.dict()]

class gridSort:
    """
    Class GridSort:
    Returns Grid Sort Format
    sort = gridSort("ATTRIBUTE", ORDER)
    .list() - RETURNS THE FINAL FORMAT [{"Attribute": "ATTRIBUTE", "Order": ORDER}] DICT IN LIST
    .dict() - RETURNS ONLY THE DICT TO BE PUT IN A LIST {"Attribute": "ATTRIBUTE", "Order": ORDER} DICT
    Order = 1 ; Ascending <
    Order = 0 ; Descending >
    """
    def __init__(self, attribute: str, order: int):
        self.attribute = attribute
        self.order = order
    
    def dict(self):
        return {
            "Attribute": self.attribute,
            "Order": self.order
        }

    def list(self):
        return [self.dict()]


class getGridData:
    """
    Class getGridData:
    Returns a JSON formatted string for a given gridID, conditions, sort, startIndex, and recordCount
    StartIndex : Where The Data Will Begin To Load Relative To The Sort & RecordCount
    RecordCount : How Many Records Will Be Returned. TCR Does 5, 100, & 250 Records Per Page. But I Can Do More ;) but at what cost?
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    condition1 = gridCondition("StartDate", 6, v1=["01/01/2100"])
    condition2 = gridCondition("EndDate", 4, v1=["01/02/2100"])
    allConditions = [condition1.dict(), condition2.dict()]
    sortPost = gridSort("TimeSetBy", 0).list()
    post = postData(
        gridID = 54,
        conditions= allConditions,
        sort = sortPost,
        startIndex= 1,
        recordCount = 250
        )
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Can Perform:
    post.dict() - Returns The Dictionary That Would Need To Be Converted To JSON before sending to TCR
    post.json() - Returns The JSON String That Would Be Sent to TCR
    post.request() - Returns The TCR Response in JSON Format with Keys: "RecordCount", "Data"
    """
    def __init__(self, gridID, conditions, sort, startIndex, recordCount):
        self.gridID = gridID
        self.conditions = conditions
        self.sort = sort
        self.startIndex = startIndex
        self.recordCount = recordCount
        
    def listAttributes(self):               # THIS NEEDS TO BE HANDLED DIFFERENTLY
        typeFind = type(self.gridID)
        if typeFind == str:
            query = {'_id': self.gridID}
        if typeFind == int:
            query = {'GridID': self.gridID}
        location = dbGetGrid.find_one(query, {
            "Columns": 1
            })
        returnList = []
        for item in location['Columns']:
            returnList.append(item['DataField'])
        return returnList

    def dict(self):
        return {"query": {
            "GridID": self.gridID,
            "Attributes": self.listAttributes(),
            "Filter": {
                "Conditions": self.conditions
            },
            "Sort": self.sort,
            "CustomSort": None,
            "StartIndex": self.startIndex,
            "RecordCount": self.recordCount
        }}

    def json(self):
        return json.dumps(self.dict())

    def request(self, JSONReturn=True):
        if JSONReturn is True:
            request = requests.post(url=urlGetGridData, headers=headers, data=self.json())
            load = json.loads(json.loads(request.text)["d"]["Result"])
            return load
        if JSONReturn is False:
            return requests.post(url=urlGetGridData, headers=headers, data=self.json())
