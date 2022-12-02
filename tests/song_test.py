import unittest
from classes.room import *
from classes.guest import *
from classes.song import *

class TestSong(unittest.TestCase):
    def setUp(self):
        self.guest = Guest()
        self.room = Room()
        self.song = Song() 