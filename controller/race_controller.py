import json
from controller.db_controller import *
from controller.horse_controller import *
import os
import random
from datetime import datetime

class RaceController:
    def race_create_item(race_name):
        dbclient = MongoDb(os.getenv('DATABASE_NAME'), os.getenv('DATABASE_HOST'), 
                           os.getenv('DATABASE_USERNAME'), os.getenv('DATABASE_PASSWORD'))
        try:
            now = datetime.now()
            date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
            all_horses = dbclient.find_random_horses()
            
            results = [doc for doc in all_horses]
            index = random.randint(0, 5)
            winner = results[index]
            dbclient.add_new_race(race_name, date_time, winner["id"], winner["name"])  
            
            #find winner info and update is wins
            info_winner = list(dbclient.find_one_horse(winner["id"]))
            result_horse = info_winner[0]
            new_wins = int(result_horse["wins"])+1
            for info in info_winner:
                update = dbclient.update_one_horse(info["id"], info["name"], 
                                                 int(info["age"]), new_wins)
            
            return info_winner  
        except Exception as e:
            return str(e)

    def races_results():
        dbclient = MongoDb(os.getenv('DATABASE_NAME'), os.getenv('DATABASE_HOST'), 
                           os.getenv('DATABASE_USERNAME'), os.getenv('DATABASE_PASSWORD'))
        try:
            last_races = dbclient.find_last_races()
            results = [doc for doc in last_races]
            return results 
        except Exception as e:
            return str(e)