from requests import post
from config import CONFIG as config

BILLING_API = config['BILLING_API']


def payment(params):
    url = BILLING_API.get('URL') + BILLING_API.get('transactionPath')
    data = {
        "type": "CustomerPayment",
        "business": params.get('BUSINESS_ID'),
        "amount": params.get('LMI_PAID_AMOUNT'),
        "paymentInfo": dict([{param, params.get(param)} for param in params])
    }
    print(url, data)
    req = post(url, json=data, timeout=10)
    return(req)

