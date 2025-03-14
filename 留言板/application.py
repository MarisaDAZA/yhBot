from flask import Flask, request
from yunhuBot import Openapi

bot = Openapi('xxxxxxxxxx') # 填入你的token
messages = []

app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello World!'

@app.route("/yunhu", methods=['POST'])
def yunhu():
    data = request.get_json()
    if data['header']['eventType'] != 'message.receive.normal':
        return ''
    
    text = data['event']['message']['content']['text']
    senderNickname = data['event']['sender']['senderNickname']
    chatId = data['event']['chat']['chatId']
    
    if chatId == '375463881':
        messages.append('___' + senderNickname + '___**:** ' + text)
        if len(messages) > 5:
            del messages[:1]

        bot.setBoard('375463881', 'markdown', '\n'.join(messages))

    return ''
