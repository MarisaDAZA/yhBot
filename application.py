from flask import Flask, request
app = Flask(__name__)
@app.route("/", methods=['POST'])
def hello():
    data = request.get_json()
    print(data)
    return data['event']['message']['content']['text']
app.run()
