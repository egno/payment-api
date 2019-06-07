from requests import post, get
from flask import Flask, request, make_response
from flask_cors import CORS
import re
import json
# from config import CONFIG as config
import logging


app = Flask(__name__)
CORS(app)

gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)


@app.route('/', methods=['POST'])
def post_transaction():
    json_data = request.get_json()
    data = request.form
    
    app.logger.info(f"IN: {data.get('LMI_SYS_PAYMENT_DATE')}: {data.get('BUSINESS_ID')} - {data.get('LMI_PAID_AMOUNT')}. {data}")

    return make_response(json.dumps({'transaction': 'OK'}), 200, {'Content-Type': 'application/json'})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
