from requests import post
from dotenv import load_dotenv
import os

load_dotenv()

UNO_COMMISSION_PERCENT = float(os.getenv('PAYMENT_COMISSION', 0.0))
BILLING_API = {
        'URL': os.getenv('BILLING_API_URL'),
        'transactionPath': '/transaction'
    }


def payment(params, provider=None):
    url = BILLING_API.get('URL') + BILLING_API.get('transactionPath')
    print(params)
    unoCommission = round((float(params.get('LMI_PAID_AMOUNT') or 0.0) * UNO_COMMISSION_PERCENT / 100), 4)
    data = {
        "type": "CustomerPayment",
        "provider": provider,
        "business": params.get('BUSINESS_ID'),
        "amount": params.get('LMI_PAID_AMOUNT'),
        "unoCommission": unoCommission,
        "paymentInfo": dict([param, params.get(param)] for param in params)
    }
    print(url, data)
    req = post(url, json=data, timeout=10)
    return(req)

