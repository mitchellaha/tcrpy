# Get Grid Data Filtering

# Filtering

TCRAPI.Filter()

## Filtering Examples

### Example 1

Example 1 Shows a bare minimum filter query.

#### JSON Example

1. The JobID field
2. Is Equal To 
3. The Value of 958555

```jsonc
{
    "Filter":{  // FILTER ROOT WILL NOT BE CREATED
        "Conditions":[
            {
                "Attribute":"JobID",  // Field Name
                "Operator":1,      // 1 = Equal
                "Values":[
                    958555    // Job ID
                ]
            }
        ]
    }
}
```

#### How to Build with Python

```python
from TCRAPI.models import Filter

jobID_filter = Filter(
    attribute="JobID",
    operator=1,
    values=[958555]
)
print(jobID_filter.dict())
>>> {
>>>     "Conditions": [
>>>         {
>>>             "Attribute": "JobID",
>>>             "Operator": 1,
>>>             "Values": [958555]
>>>         }
>>>     ]
>>> }
```

### Example 2

Example 2 is using the advanced search function on TCR.

1. The Status of the Job is Either "O" or "P"
2. The Last Ticket Is After "01/01/2017"
3. Search Query Should return results that match both filters.
```jsonc
{
    "Filter":{  // FILTER ROOT WILL NOT BE CREATED
        "Conditions":[
            {
                "Attribute":"Status",  // Field Name. ( Status of the Job )
                "Operator":12,  // 12 = Oneof from Query Param Operators (Status Should Be Equal To One of the Values)
                "Values":[
                    "O",  // Open
                    "P"  // Pending
                ]
            }
        ],
        "Filter":{
            "Conditions":[
                {
                    "Attribute":"LastTicket",  // Advanced Search LastTicket Field
                    "Operator":6,  // GreaterThanOrEqual from Query Param Operators (On Or After for Date)
                    "Values":[
                        "01/01/2017"  // The Date to Search For
                    ]
                }
            ]
        },
        "GroupOperator":1  // 1 = AND so Query should return results that match both conditions. See Query Group Operator
    }
}
```

#### How to Build with Python

    
```python
from TCRAPI.models import Filter

multiFilter = Filter(
    attribute="Status",
    operator=12,
    values=["O", "P"]
).add_advanced_filter(
    Filter(
        attribute="LastTicket",
        operator=6,
        values=["01/01/2017"]
    ).set_group_operator(1)
)
```



### Example 3

Example 3 is using the quick seach function on TCR.

1. The Status of the Job is Either "O" or "P"
2. Internal Group Operator is 2, so The search query should match any of the conditions with values "TEST"

```jsonc
{
    "Filter":{  // FILTER ROOT WILL NOT BE CREATED
        "Conditions":[
            {
                "Attribute":"Status",  // Field Name. ( Status of the Job )
                "Operator":12,  // 12 = Oneof from Query Param Operators (Status Should Be Equal To One of the Values)
                "Values":[
                    "O",  // Open
                    "P"  // Pending
                ]
            }
        ],
        "Filter":{
            "GroupOperator":2,  // 2 = OR so Query should return results that match either condition below. See Query Group Operator
            "Conditions":[
                {
                    "Attribute":"CustomerCode",  //  CustomerCode Field
                    "Operator":10,  // 10 = Contains from Query Param Operators
                    "Values":[
                        "TEST"  // The Value to Search For
                    ]
                },
                {
                    "Attribute":"CustomerName",  //  CustomerName Field
                    "Operator":10,  // 10 = Contains from Query Param Operators
                    "Values":[
                        "TEST"  // The Value to Search For
                    ]
                }
            ]
        }
    }
}
```

#### How to Build with Python

```python
from TCRAPI.models import Filter

quickSearchFilter = Filter(
    attribute="Status",
    operator=12,
    values=["O", "P"]
).add_advanced_filter(
    Filter().add_quick_search_filter(
        SearchQuery="TEST",
        ListOfAttributes=["CustomerCode", "CustomerName"]
    )
)
```

# Sort 


## Sort Examples

### Example 1

Sort Ascending by OrderType

```jsonc
{
    "Sort":[
        {
            "Attribute":"OrderType",
            "Order":1
        }
    ]
}
```

#### How to Build with Python

```python
from TCRAPI.models import Sort

gridSort = Sort(Attribute="OrderType", Order=1).list()
print(gridSort)
>>> [
>>>     {
>>>         "Attribute": "OrderType",
>>>         "Order": 1
>>>     }
>>> ]
```


# Filtering Info


### Grid Filter Data Types

- 1 = Text
- 2 = Date
- 3 = Number
- 4 = PickList
- 5 = Lookup
- 6 = MultiLabels

### Query Filter Field Datatype

- 1 = ID 
- 2 = Money
- 3 = Text
- 4 = Date
- 5 = CheckboxRadio
- 6 = Lookup
- 7 = Number

### Query Group Operator

- 1 = And
- 2 = Or

### Query Param Operators

- 1 = Equal
- 2 = NotEqual
- 3 = LessThan
- 4 = LessThanOrEqual
- 5 = GreaterThan
- 6 = GreaterThanOrEqual
- 7 = Between
- 8 = StartsWith
- 9 = EndsWith
- 10 = Contains
- 11 = NotContains
- 12 = Oneof
- 13 = NotOneof
- 14 = IsNull
- 15 = NotNull

### Query Sort

- 1 = ASC
- 2 = DESC