from qwen import get_response
from flask import Flask, request
import requests
import json

def sendMessage(recvId: str, recvType: str, contentType: str, content: dict):
        token = '' # Put your token here.
        params = {
            "recvId": recvId,
            "recvType": recvType,
            "contentType": contentType,
            "content": content
         }
        headers = {'Content-Type': 'application/json'}
        return requests.post('https://chat-go.jwzhd.com/open-apis/v1/bot/send?token=' + token,headers=headers, data=json.dumps(params))


app = Flask(__name__)

@app.route("/yunhu", methods=['POST'])
def yunhu():
    data = request.get_json()
    text = data['event']['message']['content']['text']
    sender = data['event']['sender']['senderNickname']
    if data['header']['eventType'] != 'message.receive.normal':
         return ''
    if data['event']['chat']['chatType'] == 'bot':
         sendMessage('7525795','user','text',{'text': sender + '：' + text})
         sendMessage(data['event']['sender']['senderId'],'user','text',{'text': get_response(text).choices[0].message.content})
    elif data['event']['chat']['chatId'] == '375463881':
         sendMessage('7525795','user','text',{'text': sender + '（群聊消息）：' + text})
         sendMessage('375463881','group','text',{'text': get_response(text).choices[0].message.content})
    #with open("request.json", "w", encoding="utf-8") as file:
    #    json.dump(data, file, ensure_ascii=False, indent=4)
    return ''

if __name__ == "__main__":
    app.run()
