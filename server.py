import json
import time
from flask import Flask, request
app = Flask(__name__)

act_map = {}

@app.route('/')
def index():
    return json.dumps(act_map)

@app.route('/ping', methods=['GET', 'POST'])
def ping():
    body = 0
    if request.method == 'POST':
        data = request.get_data()
        data = json.loads(data)
        if not data.get('ip'):
            body = 1
        else:
            act_map[data['host']] = data
    return str(body)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
