import requests
import json

token = "" #填入你的token
headers = {"Content-Type": "application/json; charset=utf-8"}
recvId = "7525795"
recvType = "user"

def set_recvId(Id):
    global recvId
    recvId = Id
    global recvType
    if len(Id) == 9:
        recvType = "group"
    elif len(Id) == 7:
        recvType = "user"
    else:
        raise ValueError('Invalid recvId!')


def send(content):
    data_raw = {
        "recvId": recvId,
        "recvType": recvType,
        "contentType": "text",
        "content": {
            "text": content
        }
    }
    return requests.post("https://chat-go.jwzhd.com/open-apis/v1/bot/send?token=" + token,headers=headers, data=json.dumps(data_raw)).json()


def edit(content, msgId):
    data_raw = {
        "msgId": msgId,
        "recvId": recvId,
        "recvType": recvType,
        "contentType": "text",
        "content": {
            "text": content
        }
    }
    return requests.post("https://chat-go.jwzhd.com/open-apis/v1/bot/edit?token=" + token,headers=headers, data=json.dumps(data_raw)).json()

def recall(msgId):
    data_raw = {
        "msgId": msgId,
        "chatId": recvId,
        "chatType": recvType,
        }
    return requests.post("https://chat-go.jwzhd.com/open-apis/v1/bot/recall?token=" + token,headers=headers, data=json.dumps(data_raw)).json()


def messages(before):
    return requests.get("https://chat-go.jwzhd.com/open-apis/v1/bot/messages?token=" + token + "&before=" + before + "&chat-id=" + recvId + "&chat-type=" + recvType,headers=headers).json()

def print_messages(before):
    print(json.dumps(messages(before), indent=4, ensure_ascii=False))

def board(content):    
    data_raw = {
        "recvId": recvId,
        "recvType": recvType,
        "contentType": "text",
        "content": content
    }
    return requests.post("https://chat-go.jwzhd.com/open-apis/v1/bot/board?token=" + token,headers=headers, data=json.dumps(data_raw)).json()

def board_dismiss():
    data_raw = {
        "recvId": recvId,
        "recvType": recvType,
    }
    return requests.post("https://chat-go.jwzhd.com/open-apis/v1/bot/board-dismiss?token=" + token,headers=headers, data=json.dumps(data_raw)).json()
