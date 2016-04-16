import json

import requests
from flask import Flask, request, jsonify
from flask.ext.cors import CORS, cross_origin
from flask_restful import Resource, Api
from fingerprint import FingerprintClient
from module import Module

app = Flask("Fraud Service")
CORS(app)

module = Module()
fper = FingerprintClient()

@app.route('/isvirgin/', methods=['GET'])
def get_is_virgin():
    userid = request.args.get('userid')
    deviceid = request.args.get('deviceid')
    ip = request.remote_addr

    is_virgin = module.is_first_time(userid, ip, deviceid)

    return jsonify({'virgin': is_virgin})

@app.route('/userdata/', methods=['GET'])
def get_user_data():
    userid = request.args.get('userid')
    ip = request.remote_addr

    data = module.load(userid, ip)

    try:
        data['data'] = [fper.getSessionData(deviceid) for deviceid in data['deviceids']]
    except:
        return jsonify({'error': 'some errors happened, yo'})

    return jsonify(data)


@app.route('/login/', methods=['POST'])
def login_user():
    try:
        params = request.get_json(force=True)
        deviceid = params.get('deviceid')
        userid = params.get('userid')
    except:
        deviceid = request.form.get('deviceid')
        userid = request.form.get('userid')

    fper.createOrder(userid, deviceid)

    ip = request.remote_addr

    fingerprint_id = module.save(userid, deviceid, ip)

    return jsonify({
        'fingerprintid' : fingerprint_id,
        'deviceid': deviceid,
        'userid' : userid,
        'ip': ip
        })


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
