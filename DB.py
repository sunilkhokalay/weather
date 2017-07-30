import datetime
from pymongo import MongoClient

class Db:
    def __init__(self,ip="localhost",port=27017):
        self.ip = ip
        self.port = port
        client = MongoClient(self.ip,self.port)
        db = client.weather
        collection = db.temperatures
        self.posts = db.posts
        self.current_update_id = [p['sl'] for p in self.posts.find()][-1] + 1

    def update_temperature(self,temp):
        post = {'sl':self.current_update_id,'temp':temp,'TS':str(datetime.datetime.now())}
        self.posts.insert(post)
        self.current_update_id += 1
