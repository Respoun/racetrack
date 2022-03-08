import sys
import pymongo
from pymongo import MongoClient
from termcolor import colored, cprint

class MongoDb:
    def __init__(self, database_name, database_host, database_username, database_password):
        self.db_password = database_password
        self.db_user = database_username
        self.db_bhost = database_host
        self.db_name = database_name
        try:
            self.client = MongoClient("localhost", 27017, username=self.db_user, password=self.db_password)
            self.database = self.client[self.db_name]
            cprint("[+] DB connect OK", 'green', attrs=['bold'])
        except Exception as e:
            cprint(e, 'red', attrs=['bold'])
    
    def find_all_horses(self):
        collection = self.database['horses']
        cursor = collection.find({})  
        return cursor
    
    def find_one_horse(self, id_horse):
        collection = self.database['horses']
        cursor = collection.find({"id": int(id_horse)}) 
        return cursor

    def find_random_horses(self):
        collection = self.database['horses']
        cursor = collection.aggregate([
                { "$match": { "id": { "$exists": True } } },
                { "$sample": { "size": 6 } }
            ])
        return cursor

    def find_last_add_horse(self):
        collection = self.database['horses']
        cursor = collection.find({}).sort("id", -1).limit(1)
        return cursor
    
    def add_new_horse(self, mydict):
        collection = self.database['horses']
        collection.insert_one(mydict)

    def update_one_horse(self, id_horse, name_horse, age_horse, wins):
        collection = self.database['horses']
        cursor = collection.find_one_and_update({"id": id_horse}, {"$set": {"name": name_horse, "age": age_horse, "wins": wins}}, upsert=False)
        return cursor
    
    def delete_one_horse(self, id_horse):
        collection = self.database['horses']
        collection.delete_one({"id": id_horse})

    def add_new_race(self, race_name, race_date, horse_id, horse_name):
        collection = self.database['races']
        collection.insert_one({"date": race_date, "name": race_name, "horse_id": horse_id, "horse_name": horse_name})

    def find_last_races(self):
        collection = self.database['races']
        cursor = collection.find().limit(9).sort([("date", pymongo.ASCENDING)])
        return cursor