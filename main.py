import json

import requests
from flask import Flask, request, jsonify
from flask.ext.cors import CORS
from flask_restful import Resource, Api

app = Flask("Fraud Service")
CORS(app)
api = Api(app)

class FingerPrintController(Resource):

    def __init__(self):
        pass

    def get(self):
        return vars(request.args.get('id'))

    def post(self):
        params = request.get_json()
        deviceid = params.get('deviceid')
        userid = params.get('userid')
        ip = request.remote_addr

        return jsonify({'deviceid': deviceid, 'userid': userid, 'ip': ip})

api.add_resource(FingerPrintController, "/fu")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
