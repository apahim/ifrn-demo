import logging
import platform

from flask import Flask
from flask import jsonify
from flask import request


logging.basicConfig(level=logging.INFO)

APP = Flask(__name__)
LOG = logging.getLogger('cloudy')


@APP.route('/', methods=["GET"])
def root():
    LOG.info(f'[{request.method}] {request.url}')
    return jsonify(
        {
            'message': 'Hello IFRN!',
            'hostname': platform.node(),
        }
    ), 200


if __name__ == '__main__':
    APP.run(host='127.0.0.1', debug=True, port=8080)
