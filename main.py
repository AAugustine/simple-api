from flask import Flask, request, abort, jsonify
import json

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
DATA_FROM_WEBHOOK = None

@app.route('/')
def index():
    if DATA_FROM_WEBHOOK:
        return jsonify(DATA_FROM_WEBHOOK)
    else: 
        formatted_res = 'Waiting for data...'
        return 'WEBHOOK DATA: %s' % formatted_res

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        res = request.json
        print(res)
        global DATA_FROM_WEBHOOK
        DATA_FROM_WEBHOOK = res
        return res, 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run(debug=True)
