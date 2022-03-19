from GetGridData import *
import requests
import json
from common import gridDataUrl, headers


class scheduleOBJ:
    GridID = 54
    Attributes = [
        "ScheduleID",
        "ScheduleType",
        "TicketID",
        "DriverName",
        "TruckCode",
        "ScheduleDate",
        "ClockIn",
        "TimeNeeded",
        "TimeSetBy",
        "EstimatedTimeOnSite",
        "Status",
        "TicketNumber",
        "PrintStatus",
        "Description",
        "Comments",
        "CustomerCode",
        "CustomerName",
        "JobNumber",
        "JobAddress1",
        "City",
        "Foreman",
        "ForemanPhone",
        "DispatcherName",
        "JobName",
        "ProjectManagerName",
        "PONumber",
        "ForemanCompany",
        "StartAddress",
        "EndAddress"
    ]

    def payload(self, Start, End, StartIndex=1, RecordCount=150):
        scheduleData = Root(
            query=Query(
                GridID=self.GridID,
                RecordCount=RecordCount,
                Filter=Filter(
                    Conditions=[
                        Conditions(
                            Attribute="StartDate",
                            Values=[
                                str(Start)
                            ],
                            Operator=6
                        ),
                        Conditions(
                            Attribute="EndDate",
                            Values=[
                                str(End)
                            ],
                            Operator=6
                        ),
                        Conditions(
                            Attribute="BranchID",
                            Values=[
                                ""
                            ],
                            Operator=1
                        ),
                        Conditions(
                            Attribute="Status",
                            Values=[
                                ""
                            ],
                            Operator=1
                        ),
                        Conditions(
                            Attribute="TransactionID",
                            Values=[
                                ""
                            ],
                            Operator=1
                        ),
                        Conditions(
                            Attribute="RecordType",
                            Values=[
                                1
                            ],
                            Operator=1
                        )
                    ]
                ),
                StartIndex=StartIndex,
                Attributes=self.Attributes,
                Sort=[
                    Sort(
                        Attribute="TimeSetBy",
                        Order=1
                    )
                ],
                CustomSort=None,
            )
        ).json()
        return scheduleData

    def getSchedule(self, start, end, StartIndex=1, RecordCount=150):
        scheduleData = self.payload(start, end, StartIndex, RecordCount)
        response = requests.post(
            gridDataUrl, headers=headers, data=scheduleData).json()
        resultjson = json.loads(response["d"]["Result"])
        count = resultjson["RecordCount"]
        data = resultjson["Data"]
        return count, data
