from flask import Flask, request
from qwen import qwenChat
import requests
import json
import openai

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

def chat(Id: str, text: str, chatType: str):
    if Id not in messages.keys():
        messages[Id] = []
    messages[Id].append({"role": "user","content": text})
    try:
        output = qwenChat(messages[Id]).choices[0].message.content
    except openai.BadRequestError:
        messages[Id] = []
        return

    if '```' in output:
        sendMessage(Id,chatType,'markdown',{'text': output})
    else:
        sendMessage(Id,chatType,'text',{'text': output})
    messages[Id].append({"role": "assistant","content": output})
    if len(messages[Id]) >= 8:
        del messages[Id][:2]
    # with open("messages.txt", "w") as file:
    #     json.dump(messages, file, ensure_ascii=False, indent=4)

# try:
#     with open("messages.txt", "r") as file:
#         messages = json.load(file)
# except json.decoder.JSONDecodeError:
#     messages = {}
messages = {}

app = Flask(__name__)

@app.route("/yunhu", methods=['POST'])
def yunhu():
    data = request.get_json()
    if data['header']['eventType'] != 'message.receive.normal':
        return ''
    
    text = data['event']['message']['content']['text']
    senderNickname = data['event']['sender']['senderNickname']
    senderId = data['event']['sender']['senderId']
    chatId = data['event']['chat']['chatId']
    chatType = data['event']['chat']['chatType']
    
    if chatType == 'bot':
        # sendMessage('7525795','user','text',{'text': senderNickname + '：' + text})
        chat(senderId, text, 'user')
        

    elif chatId == '375463881':
        sendMessage('7525795','user','text',{'text': '[云湖新闻站]' + senderNickname + '：' + text})
        chat('375463881', text, 'group')

    elif text[0] == '.':
        chat(chatId, text[1:], 'group')

    return ''

if __name__ == "__main__":
    app.run()
