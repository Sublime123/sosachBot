import bot.longPoll as longPoll
import bot.settings as settings
import bot.db as db
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
        self.storage = db.Storage(self.settings.debug)
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
                messageText = event['object']['message']['text']
                conferenceId = event['object']['message']['peer_id']
                senderId = event['object']['message']['from_id']
                if (messageText == '!pidor' or messageText == '!пидор'):
                    #self.longPoll.sendMessage(conferenceId,'Вы все пидоры')
                    response = self.longPoll.getMembers(conferenceId)
                    countOfUsers = response["response"]["count"]
                    luckyNum = random.randint(0, countOfUsers)
                    text = "Пидор [id" + str(response["response"]["profiles"][luckyNum]["id"]) + "|" + \
                        response["response"]["profiles"][luckyNum]["first_name"] + "]!"
                    #print(text)
                    self.storage.raiseCountOnUser(conferenceId=conferenceId,\
                                                  userVkId=response["response"]["profiles"][luckyNum]["id"],\
                                                  name=response["response"]["profiles"][luckyNum]["first_name"],\
                                                  lastName=response["response"]["profiles"][luckyNum]["last_name"])
                    self.longPoll.sendMessage(conferenceId,text)
                elif (messageText == '!stat' or messageText == '!статистика' or messageText == '!стат'):
                    conferenceId = conferenceId
                    stat = self.storage.getConferenceStat(conferenceId)
                    text = ""
                    if (len(stat) != 0):
                        text = "Пидоры конференции: \n"
                        for person in stat:
                            text += person['name'] + " пидор " + str(person['count']) + " раз\n"
                    else:
                        text = "Никто ещё не стал пидором."
                    self.longPoll.sendMessage(conferenceId,text)
                elif (messageText == '!roulette' or messageText == '!рулетка'):
                    if (random.randint(0, 1) == 0):
                        shot = True
                    else:
                        shot = False
                    if shot == True:
                        text = '[id' + str(senderId) + '|Ты] ' +  'отстрелил себе башку, тупица!'
                    else:
                        text = 'Пронесло'
                    self.longPoll.sendMessage(conferenceId,text)
                    
    def requestLoop(self):
        while self.execute:
            if self.longPoll.initialized != True:
                self.longPoll.getLongPoll()
                if self.longPoll.initialized != True:
                    break
            self.longPoll.longPoll()
    
