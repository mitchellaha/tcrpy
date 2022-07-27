from typing import Any, List

from pydantic import BaseModel, conint


class GetGridDataModel(BaseModel):
    GridID: int
    RecordCount: conint(ge=50) = 50
    Filter: dict = {}
    StartIndex: conint(ge=1) = 1
    Attributes: List[str]
    Sort: list = []
    CustomSort: Any = None

class GetGridDateRootModel(BaseModel):
    query: GetGridDataModel


class Filter:
    """
    Used to create filter conditions for the getGrid API Call.
    """
    def __init__(self, Attribute: str = None, Operator: int = None, Values: list = None, **kwargs):
        self.Conditions = []

        if Attribute is not None and Operator is not None and Values is not None:
            self.add_condition(Attribute, Operator, Values)

        if "Conditions" in kwargs.keys():
            self.Conditions = kwargs["Conditions"]
        if "Filter" in kwargs.keys():
            self.Filter = kwargs["Filter"]
        if "GroupOperator" in kwargs.keys():
            self.GroupOperator = kwargs["GroupOperator"]


    def add_condition(self, Attribute: str, Operator: int, Values: list):
        """
        Adds a condition to the filter.
        
        params
        --------
        attribute: str
            The attribute to filter on.
                ex. "OrderType"
        value: list
            The value to filter on.
                ex. ["Name"] or ["Date", "Date"]
        operator: int
            The operator to use.
                ex. <SEE OPERATOR DOCUMENTATION>
        """
        self.Conditions.append({
            "Attribute": Attribute,
            "Operator": Operator,
            "Values": Values
        })
        return self

    def add_advanced_filter(self, filter):
        """
        Adds a Filter Class inside this Filter Class.
        
        params
        --------
        filter: Filter Object or dict
            The filter to add.
        """
        if isinstance(filter, Filter):
            self.Filter = filter.dict()
        elif isinstance(filter, dict) and "Conditions" in filter.keys():
            self.Filter = filter
        else:
            raise TypeError("Filter must be of type Filter or dict.")
        return self

    def set_group_operator(self, Operator: int):
        """
        Adds a group operator to the filter.
        Group Operators are Only Used When Adding Quick Search Filters.
            
        params
        --------
        operator: int
            The operator to use.
        """
        self.GroupOperator = Operator
        return self

    def add_quick_search_filter(self, SearchQuery, ListOfAttributes, GroupOperator = 2):
        """
        Adds Many Search Conditions to the Filter.

        params
        --------
        SearchQuery: str
            The search query to use.
        ListOfAttributes: list
            The list of attributes to search on.
        GroupOperator: int (optional)
            - 1 = AND
            - 2 = OR (Default)

        Example:
        --------
            >>> searchFilterEx = Filter()
            >>> searchFilterEx.AddSearchFilter("MyName", ["Drivers", "JobLocation", "CustomerName"])
            >>> searchFilterEx.dict()
            {
                "Conditions": [
                    {
                        "Attribute": "Drivers",
                        "Operator": 10,
                        "Values": ["MyName"]
                    },
                    {
                        "Attribute": "JobLocation",
                        "Operator": 10,
                        "Values": ["MyName"]
                    },
                    {
                        "Attribute": "CustomerName",
                        "Operator": 10,
                        "Values": ["MyName"]
                    }
                ],
                "GroupOperator": 2
            }
        """
        self.GroupOperator = GroupOperator
        for attribute in ListOfAttributes:
            self.add_condition(attribute, 10, [SearchQuery])
        return self

    def dict(self):
        """
        Returns the filter as a dictionary.
        """
        return self.__dict__

    def __repr__(self):
        return str(self.__dict__)

    def __str__(self):
        return self.__repr__()



class Sort:  # TODO: Does this Need to be Redone to add multiple sorts??
    """
    Used to create sort conditions for the getGrid API Call.

    Example:
    --------
        >>> gridSort = Sort(Attribute="OrderType", Order=1)
        >>> gridSort.list()
        [
            {
                "Attribute": "OrderType",
                "Order": 1
            }
        ]
    """
    def __init__(self, Attribute: str, Order: int):
        self.Attribute = Attribute
        self.Order = Order

    def dict(self):
        """
        Returns the sort as a dictionary.
        """
        return self.__dict__

    def list(self):
        """
        Returns the sort as a list.
        """
        return [self.__dict__]

    def __repr__(self):
        return str(list)

    def __str__(self):
        return self.__repr__()
