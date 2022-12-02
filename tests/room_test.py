import unittest
from classes.room import Room
from classes.guest import *
from classes.song import *

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.guest1 = Guest("Dan", "Purple Rain", 10)
        self.guest2 = Guest("John", "Sail", 15)
        self.guest3 = Guest("Gareth", "Sail", 5)
        self.guest4 = Guest("Sam", "Sail", 50)
        self.song1 = Song("Purple Rain", "Prince")
        self.song2 = Song("Be my baby", "Ronettes")
        self.song3 = Song("I want it that way", "Backstreet boys")
        self.room = Room()

    def test_guest_has_checked_in(self):
        self.room.guests_check_in(self.guest1)
        self.room.guests_check_in(self.guest2)
        guest_amount = self.room.guest_in_room()
        self.assertEqual(2, guest_amount)

    def test_guest_checked_out(self):
        self.room.guests_check_in(self.guest1)
        self.room.guests_check_out(self.guest1)
        guest_amount = self.room.guest_in_room()
        self.assertEqual(0, guest_amount)

    def test_songs_added_to_list(self):
        # self.room.add_songs(self.song1)
        # self.room.add_songs(self.song2)
        # self.room.add_songs(self.song3)
        # self.assertEqual(3, len(self.room.list_of_songs))
        pass

    def test_too_many_people_want_to_sing(self):
        self.room.guests_check_in(self.guest1)
        self.room.guests_check_in(self.guest2)
        self.room.guests_check_in(self.guest3)
        self.room.guests_check_in(self.guest4)
        capacity = self.room.guest_capacity()
        self.assertEqual(False, capacity)

    def test_customer_pays_for_room(self):
        self.room.guests_check_in(self.guest1)
        self.assertEqual(105, self.room.till)
        self.assertEqual(5, self.guest1.wallet)

    def test_customer_finds_fav_song(self):
        self.room.guests_check_in(self.guest1)
        self.room.guests_check_in(self.guest2)
        self.room.add_songs(self.song1)
        self.room.add_songs(self.song2)
        guest_response = self.room.sees_fav_song()
        self.assertEqual("Whoo!", guest_response)
