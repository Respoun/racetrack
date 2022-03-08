import unittest
from view.view import View
from controller.race_controller import *

#Sample test class to demonstrate
class TestFake(unittest.TestCase):

    def test_option6_create_race(self):
        race_name = "La super course"
        #Create race
        race = RaceController.race_create_item(race_name) 
        
        self.assertTrue(race["id"])

    def test_option7_view_last_result(self):
        race_name = "La super course"
        #Create race
        race = RaceController.race_create_item(race_name) 

        all_races = RaceController.races_results()   
        
        self.assertTrue(all_races)