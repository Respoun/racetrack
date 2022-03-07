from controller.horse_controller import *
from controller.race_controller import *

class View:
    def add_horse_view():
        print("Choose a horse name:")
        name = str(input())
        print("Choose a horse age:")
        age = int(input())
        add_horse = HorseController.horse_add_item(name, age)
        return add_horse 

    def read_horse_view():
        print("Choose a horse id:")
        id = str(input())
        read_horse = HorseController.horse_read_item(id)
        return read_horse 

    def read_horses_view():
        read_horses = HorseController.horse_read_items()
        return read_horses 
    
    def updade_horse_view():
        print("Choose a horse id:")
        id_horse = int(input())
        print("Choose a horse name:")
        name_horse = str(input())
        print("Choose a horse age:")
        age_horse = int(input())
        print("Choose a horse wins number:")
        wins = int(input())
        update_horse = HorseController.horse_update_item(id_horse, name_horse, age_horse, wins)
        return name_horse

    def delete_horse_view():
        print("Choose a horse id:")
        id_horse = int(input())
        delete_horse = HorseController.horse_delete_item(id_horse)        
        return id_horse

    def start_race_view():
        print("Choose a Race Name:")
        race_name = str(input())
        race = RaceController.race_create_item(race_name)        
        return race
    
    def last_results_race_view():
        races = RaceController.races_results()        
        return races