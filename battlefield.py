from fleet import Fleet
from herd import Herd
import random
from robot import Robot
from dinosaur import Dinosaur

class Battlefield:

    def __init__(self):
        self.fleet = Fleet
        self.herd = Herd

    def run_game(self):
        pass

    def display_welcome(self):
        self.welcome_player = "Welcome to Robots vs. Dinosaurs!"

    def battle(self):
        self.begin_battle = random(Fleet, Herd)

    def dino_turn(self, dinosaur):
        self.select_dino = [Dinosaur]

    def robo_turn(self, robot):
        self.select_robo = [Robot]

    def show_dino_opponent_options(self):
        self.dino_opponent = [Dinosaur]

    def show_robo_opponent_options(self):
        self.robo_opponent = [Robot]

    def display_winners(self):
        pass