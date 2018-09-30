import os
from flask import Flask


app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>', methods=['GET'])
def hello_name(name):
    # name is variable not string, corrected
    return "Hello {}! Welcome!!".format(name)

if __name__ == "__main__":
    # server_tier is to select different host address, local or server
    server_tier = os.environ.get('SERVER_TIER') or 'LOCAL'
    if server_tier in ['LOCAL']:
        app.run(host='127.0.0.1', port=5000)
    else:
        app.run(host='0.0.0.0', port=5000)