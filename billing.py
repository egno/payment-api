from requests import post
from config import CONFIG as config

BILLING_API = config['BILLING_API']
UNO_COMISSION_PERCENT = config['unoComissionPrecent'] or 0.0


def payment(params):
    url = BILLING_API.get('URL') + BILLING_API.get('transactionPath')
    print(params)
    unoComission = round((float(params.get('LMI_PAID_AMOUNT') or 0.0) * UNO_COMISSION_PERCENT / 100), 4)
    data = {
        "type": "CustomerPayment",
        "business": params.get('BUSINESS_ID'),
        "amount": params.get('LMI_PAID_AMOUNT'),
        "unoComission": unoComission,
        "paymentInfo": dict([{param: params.get(param)} for param in params])
    }
    print(url, data)
    req = post(url, json=data, timeout=10)
    return(req)

