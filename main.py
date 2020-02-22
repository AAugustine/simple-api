from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/')
def main():
    return 'Hello, World!'

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        res = request.json
        print(res)

        return res, 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run(debug=True)