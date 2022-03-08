import unittest
from view.view import View
from controller.horse_controller import *

#Sample test class to demonstrate
class TestFake(unittest.TestCase):

    def test_option1_add_horse(self):
        name = "Findus"
        age = 7
        #Add horse
        add_horse = HorseController.horse_add_item(name, age)
        
        self.assertEqual(add_horse["name"], "Findus")

        #for horse in view_add_horse:
        #    self.assertEqual(horse["name"], "Findus")

    def test_option2_view_one_horse(self):
        name = "Jack"
        age = 9
        #Add horse
        add_horse = HorseController.horse_add_item(name, age)

        #Read horse
        read_horse = HorseController.horse_read_item(id)

        self.assertEqual(read_horse["name"], "Jack")
)
    def test_option4_update_one_horse(self):
        name = "Tommy"
        age = 9
        #Add horse
        add_horse = HorseController.horse_add_item(name, age)

        id = add_horse["id"]
        name = "Pierre"
        age = 9
        wins = add_horse["wins"]

        #Update horse
        update_horse = HorseController.horse_update_item(id, name, age, wins)

        self.assertEqual(update_horse["name"], "Pierre")
