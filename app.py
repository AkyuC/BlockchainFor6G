from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/api/value', methods=['POST'])
def set_value():
    key = request.json.get('key')
    value = request.json.get('value')

    command = 'node write.js {0} {1}'.format(int(key),value)
    with os.popen(command) as nodejs:
        result = nodejs.read().replace('\n','')
    print(result)

    response = {
        'message': 'Value set successfully',
        'key': key,
        'value': value
    }
    return jsonify(response), 200

@app.route('/api/value', methods=['GET'])
def set_value():
    key =  request.args.get('key')

    command = 'node read.js {0}'.format(int(key))
    with os.popen(command) as nodejs:
        result = nodejs.read().replace('\n','')
    print(result)   

    response = {
        'message': 'Value get successfully',
        'key': key,
        'value': result
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)