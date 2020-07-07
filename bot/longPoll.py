import requests
from queue import Queue
import random

class LongPoll:
    def __init__(self,basicToken,groupId,debug=False,verbouse=False):
        self.longpollApi = 'https://api.vk.com/method/groups.getLongPollServer'
        self.messageApi = 'https://api.vk.com/method/messages.send'
        self.groupId = groupId
        self.basicToken = basicToken
        self.LongpollServer = None
        self.longPollToken = None
        self.debug = debug
        self.verbouse = verbouse
        self.ts = None
        self.waitDefalt = 25
        self.initialized = False
        self.longpoolRes = Queue()
        self.longpoolResMax = 10
    def getLongPoll(self):
        try:
            print(self.basicToken)
            answer = requests.post(\
                self.longpollApi,\
                data = {'group_id':self.groupId ,\
                        'access_token':self.basicToken,\
                        'v':'5.110'})
        except requests.ConnectionError:
            if (self.debug == True):
                print("Connection Error" + "\n")
            return
        if (answer.status_code == 200):
            if (self.debug == True):
                print("Longpoll: 200, answer:" + answer.text + "\n")
            ansJson = answer.json()
            self.LongpollServer = ansJson["response"]["server"]
            self.longPollToken = ansJson["response"]["key"]
            self.logPollToken = ansJson["response"]["ts"]
            self.initialized = True
        else:                
            if (self.debug == True):
                print("Longpoll status: " + str(anwer.status_code) + "\n" )
            raise Exception("Status code is incorrect ")
    def longPoll(self):
        if (self.longpoolRes.qsize() < self.longpoolResMax):
            res = requests.post(self.LongpollServer, data = {\
                    'act':'a_check','key':self.longPollToken,\
                    'ts':self.ts,'wait':self.waitDefalt})
            if (res.status_code == 200):
                json = res.json()  
                self.ts = json['ts']
                failed = False
                try: 
                    if (json['failed'] == 1):
                        failed = True
                except:
                    pass
                if (failed == False):
                    self.longpoolRes.put(json['updates'])
            else:
                raise Exception("Status code is incorrect")
    def sendMessage(self,dialog,text):
        resMsgRes = requests.post(self.messageApi, data = {\
            'peer_id':dialog, 'group_id':self.groupId, 'message':text,\
            'random_id':random.randint(1, 1000), 'access_token':self.basicToken, 'v':'5.123'})
        if self.debug == True:
            print(resMsgRes.text)
    def getParticipiants(self,dialog):
        pass
