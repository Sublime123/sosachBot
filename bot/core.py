import bot.longPoll as longPoll
import bot.settings as settings
import os
import asyncio
from threading import Thread
import bot.messages as messages
import random

class Core:
    def __init__(self):
        # Read settings
        self.settings = settings.Settings(keys = "keys", \
                                          settings = ".")
        self.longPoll = longPoll.LongPoll(self.settings.basicToken,\
                                          self.settings.groupID,\
                                          self.settings.debug)
        self.longPollThread = None
        self.execute = False
        self.work = True
    
    def eventLoop(self):
        while self.work:
            self.handleData(self.longPoll.longpoolRes.get())
    
    def run(self):
        self.longPollThread = Thread(target=self.requestLoop)
        self.execute = True
        self.longPollThread.start()
        self.eventLoop()
        
    def handleData(self, dataPart):
        if (self.settings.verbouse == True):
            print(dataPart)
        for event in dataPart:
            if (event['type'] == "message_new"):
                if (event['object']['message']['text'] == '!pidor'):
                    #self.longPoll.sendMessage(event['object']['message']['peer_id'],'Вы все пидоры')
                    response = self.longPoll.getMembers(event['object']['message']['peer_id'])
                    luckyNum = random.randint(0, response["response"]["count"])
                    text = "Пидор [id" + str(response["response"]["profiles"][luckyNum]["id"]) + "|" + \
                        response["response"]["profiles"][luckyNum]["first_name"] + "]!"
                    #print(text)
                    self.longPoll.sendMessage(event['object']['message']['peer_id'],text)
    def requestLoop(self):
        while self.execute:
            if self.longPoll.initialized != True:
                self.longPoll.getLongPoll()
                if self.longPoll.initialized != True:
                    break
            self.longPoll.longPoll()
    
