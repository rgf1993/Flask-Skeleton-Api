from flask_skeleton import app, flaskSkeletonDAO
from flask import jsonify
from flask import Flask, request
import json
import os

@app.route('/health', methods=['GET'])
def get_health():
    result = {"result" : "Hello."}

    return jsonify(result)
