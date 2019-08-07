from flask import Flask, request, make_response
from flask_cors import CORS
import json
import logging
import billing


app = Flask(__name__)
CORS(app)

gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)


@app.route('/', methods=['POST'])
def post_transaction():

    data = request.form

    app.logger.info(f"IN: {data}")
    provider = 'paymaster'
    req = billing.payment(params=data, provider=provider)
    res = req.json()
    app.logger.info(f"RESPONSE: {res}")


    # TODO сделать проверку контрольной суммы
    # TODO сделать проверку IP отправителя


    return make_response(json.dumps({'id': res.get('transaction', {}).get('id')}), req.status_code, {'Content-Type': 'application/json'})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
