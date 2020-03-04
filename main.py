from flask import Flask, request, abort

app = Flask(__name__)
DATA_FROM_WEBHOOK = 'Waiting for data...'

@app.route('/')
def index():
    return 'WEBHOOK DATA: %s' % DATA_FROM_WEBHOOK

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