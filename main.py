from flask import Flask, jsonify
import os
import json

app = Flask(__name__)


@app.route('/')
def get_json():
    try:
        with open(os.path.join(os.path.dirname(__file__), 'api2.json'), 'r') as f:
            data = json.load(f)  
            return jsonify(data) 
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/check', methods=['GET'])
def check_status():
    return 'OK', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
