import datetime
import json
import os  # for os.path.basename
from pprint import pprint  # For debugging

import requests  # For making HTTP requests

from common import findPages, fixTime, gridDataUrl, headers, startIndex, toJSON
from tcr_py import gridCondition, gridSort


def customerPayload(StartIndex, PageSize, Status=None):
    """
    This function creates the payload for the customer API call.

        Status:
            ALL: None
            Active: "A"
            Inactive: "I"
            On Hold: "H"
            Pre-Pay: "P"
    Parameters:
        Status (str): The status of the customer.
        StartIndex (int): The starting index of the customer.
        PageSize (int): The number of customers to return.

    Returns:
        payload (dict): The payload for the customer API call.
        
    """
    attributes = [
        "CustomerID",
        "Status",
        "CustomerCode",
        "CustomerName",
        "Address1",
        "City",
        "State",
        "ZipCode",
        "Contact",
        "Phone1",
        "DateOpened",
        "SalespersonName",
        "PriceListDescription",
        "Address2",
        "Phone2",
        "Fax",
        "Email",
        "AcctContact",
        "AcctPhone",
        "AcctFax",
        "AcctEmail",
        "TaxExempt",
        "TaxExemptNo",
        "InsuranceCert",
        "InsurCertExpiration",
        "PORequired",
        "DepositRequired",
        "RentalMinAmt",
        "InvoiceFormat",
        "QBExportJobName",
        "InvoiceDOW",
        "CustomerGroup",
        "BillingCycle",
        "ExportInvoices",
        "PreliminaryNoticeRequired",
        "InvoiceEmail",
        "BusinessTypeID",
        "IncludeTicketsWithInvoice",
        "TicketLaborMinimumCharge",
        "RequirePhotoToCompleteTicket",
        "RetainagePercent",
        "InvoiceEmailSubject",
        "Comment",
        "CustomField1",
        "AccountingTermID",
        "Statements",
        "FlatRates",
        "InvoiceEmailContactID",
        "DiscountRate",
        "PONumber",
        "DateCreated",
        "CreatedBy",
        "DateUpdated",
        "UpdatedBy"
    ]
    conditions = []
    if Status is not None:
        conditions = gridCondition(attribute="Status", operator=12, v1=Status).list()
    
    sort = gridSort("DateUpdated", order=1).list()
    
    payload = {
        "query": {
            "GridID": 1,
            "Attributes": attributes,
            "Filter": {
                "Conditions": conditions
            },
            "Sort": sort,
            "CustomSort": None,
            "StartIndex": StartIndex,
            "RecordCount": PageSize
        }}
    return payload


def getCustomerData(StartIndex, PageSize, Status):
    """
    This function gets the customer data from the API.
    Parameters:
        startIndex (int): The starting index of the customer.
        pagesize (int): The number of customers to return.
        status (str): The status of the customer.

    Returns:
        count (int): The total number of customers.
        data (list): The list of customers.
    """
    payload = json.dumps(customerPayload(StartIndex, PageSize, Status=Status))
    response = requests.post(gridDataUrl, headers=headers, data=payload)
    resultjson = json.loads(json.loads(response.text)["d"]["Result"])  # Loaded The D > Response From TCR
    count = resultjson["RecordCount"]
    data = resultjson["Data"]
    return count, data

def getCustomers(Count, PageSize, Status):
    """
    This function gets all the Customers from the API.
    Parameters:
        count (int): The total number of customers.
        status (str): The status of the customer.
        pagesize (int): The number of Customer to return.

    Returns:
        data (list): The list of Customer.
    """
    data = []
    for i in range(1, findPages(Count, PageSize) + 1):
        print("Page: " + str(i) + " of " + str(findPages(Count, PageSize)))
        post = getCustomerData(startIndex(i, PageSize), PageSize, Status)
        data.extend(post[1])
    return data

if __name__ == "__main__":
    pass
