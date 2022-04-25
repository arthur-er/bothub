from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
from app.models import Message

botCache = {}

class botMaker():  
    def __init__(self, initialized=False):
        self.initialized = initialized

    def getBot(self, name, db):
        if(name in botCache):
            return botCache[name]
        else:
            chatbot = ChatBot(name, storage_adapter='chatterbot.storage.SQLStorageAdapter', database_uri='sqlite:///' + db)
            corpseTrainer = ChatterBotCorpusTrainer(chatbot)
            corpseTrainer.train("chatterbot.corpus.portuguese")
            messages = Message.query.all()
            texts = []
            for message in messages:
                texts.append(message.content)
            listTrainer = ListTrainer(chatbot)
            listTrainer.train(texts)
            botCache[name] = chatbot
            return chatbot
        

botController = botMaker()