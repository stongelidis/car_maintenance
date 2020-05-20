import os
import json

from flask import Flask, request, jsonify, abort
from database.model import setup_db


app = Flask(__name__)
setup_db(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
