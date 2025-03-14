import json
import requests
from requests_toolbelt.adapters import SourceAddressAdapter

class Openapi(object):
    """
    开放接口，用于发送消息。
    """

    # 收不到消息改serv00端口用的
    # session = requests.Session()
    # source = SourceAddressAdapter('128.204.223.119')
    # session.mount('http://', source)
    # session.mount('https://', source)


    baseUrl = "https://chat-go.jwzhd.com/open-apis/v1"
    headers = {'Content-Type': 'application/json'}

    def __init__(self, token: str) -> None:
        self.token = token
    
    def __recvType(self, recvId):
        if len(recvId) == 7:
            recvType = 'user'
        elif len(recvId) == 9:
            recvType = 'group'
        elif recvId == 'big':
            recvType = 'group'
        else:
            raise ValueError('Invalid recvId!')
        return recvType

    def sendText(self, recvId: str, text: str):
        """
        单条，发送文本消息
        """
        return self.send(recvId, "text", text)

    def sendMarkdown(self, recvId: str, text: str):
        """
        单条，发送markdown消息
        """
        return self.send(recvId, "markdown", text)
    
    def sendHtml(self, recvId: str, text: str):
        """
        单条，发送markdown消息
        """
        return self.send(recvId, "html", text)
    
    def send(self, recvId: str, contentType: str, text: str):
        """
        单条，发送单条消息
        """
        if isinstance(recvId,int):
            recvId = str(recvId)
        params = {
            "recvId": recvId, 
            "recvType": self.__recvType(recvId), 
            "contentType": contentType, 
            "content": {"text": text}
         }
        return self.session.post(self.baseUrl + '/bot/send?token=' + self.token,headers=self.headers, data=json.dumps(params))
    
    def edit(self, msgId: str, recvId: str, contentType: str, text: str):
        """
        单条，编辑单条消息
        """
        if isinstance(recvId,int):
            recvId = str(recvId)
        params = {
            "msgId": msgId, 
            "recvId": recvId, 
            "recvType": self.__recvType(recvId), 
            "contentType": contentType, 
            "content": {"text": text}
         }
        return self.session.post(self.baseUrl + '/bot/edit?token=' + self.token,headers=self.headers, data=json.dumps(params))

    def setBoard(self, recvId: str, contentType: str, text: str):
        """
        @description: 机器人看板设置接口
        机器人看板类型contentType取值: text、markdown、html
        """
        if isinstance(recvId,int):
            recvId = str(recvId)
        params = {
            "recvId": recvId, 
            "recvType": self.__recvType(recvId), 
            "contentType": contentType, 
            "content": text
         }
        return self.session.post(self.baseUrl + '/bot/board?token=' + self.token,headers=self.headers, data=json.dumps(params))
    
    def dismissBoard(self, recvId: str):
        """
        @description: 机器人看板取消接口
        """
        if isinstance(recvId,int):
            recvId = str(recvId)
        params = {
            "recvId": recvId, 
            "recvType": self.__recvType(recvId), 
         }
        return self.session.post(self.baseUrl + '/bot/board-dismiss?token=' + self.token,headers=self.headers, data=json.dumps(params))
  
