import json
from controller.db_controller import *
import os

class HorseController:
    def horse_read_items():
        dbclient = MongoDb(os.getenv('DATABASE_NAME'), os.getenv('DATABASE_HOST'), 
                           os.getenv('DATABASE_USERNAME'), os.getenv('DATABASE_PASSWORD'))
        try:
            data = dbclient.find_all_horses()
            return [item for item in data]
        except Exception as e:
            return str(e)
    
    def horse_read_item(id_horse):
        dbclient = MongoDb(os.getenv('DATABASE_NAME'), os.getenv('DATABASE_HOST'), 
                           os.getenv('DATABASE_USERNAME'), os.getenv('DATABASE_PASSWORD'))
        try:
            data = dbclient.find_one_horse(id_horse)
            return [item for item in data]
        except Exception as e:
            return str(e)
    
    def horse_add_item(name_horse, age_horse):
        dbclient = MongoDb(os.getenv('DATABASE_NAME'), os.getenv('DATABASE_HOST'), 
                           os.getenv('DATABASE_USERNAME'), os.getenv('DATABASE_PASSWORD'))
        try:
            data = dbclient.find_last_add_horse()
            for data in data:
                new_id = data["id"]+1
            mydict = {"id": new_id, "name": name_horse, "age": age_horse, "wins": 0}
            dbclient.add_new_horse(mydict)
            data_new_horses = dbclient.find_last_add_horse()
            return [item for item in data_new_horses]   
        except Exception as e:
            return str(e)
    
    def horse_update_item(id_horse, name_horse, age_horse, wins):
        dbclient = MongoDb(os.getenv('DATABASE_NAME'), os.getenv('DATABASE_HOST'), 
                           os.getenv('DATABASE_USERNAME'), os.getenv('DATABASE_PASSWORD'))
        try:
            update = dbclient.update_one_horse(id_horse, name_horse, age_horse, wins)
            return [item for item in update]
        except Exception as e:
            return str(e)
    
    def horse_delete_item(id_horse):
        dbclient = MongoDb(os.getenv('DATABASE_NAME'), os.getenv('DATABASE_HOST'), 
                           os.getenv('DATABASE_USERNAME'), os.getenv('DATABASE_PASSWORD'))
        try:
            delete = dbclient.delete_one_horse(id_horse)
            return [item for item in delete]
        except Exception as e:
            return str(e)
