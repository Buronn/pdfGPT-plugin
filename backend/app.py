from flask import Flask

from routes.plugins import plugins

import tensorflow as tf

import logging

logging.info("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

if tf.test.gpu_device_name():
    logging.info('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
else:
    logging.info("Please install GPU version of TF")


app = Flask(__name__, static_folder='static')

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = 'https://chat.openai.com'
    response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response

app.register_blueprint(plugins)