
from fleet import Fleet
from herd import Herd
import random


class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
           
    def display_welcome(self):
        self.welcome_player = "Welcome to Robots vs. Dinosaurs!"

    def battle(self):
        print("Kyle, 100"[0], "Chad, 100"[1], "Pierre, 100"[2])
        self.robot_choice = self.fleet.robot[input('Enter the number of the robot you want to play')]
        proceed = False
        while proceed == False:
            if self.robot_choice == self.fleet.robot[0]:
                proceed = True
                print(f'Your first robot is {self.fleet.robot[0]}')
        #elif self.begin_battle == self.herd:
           # print(f'Select your dinosaur {self.herd}')

    def dino_turn(self):
        attacking_dino = self.herd.dinosaur[0]
        attacked_robot = self.fleet.robot[0]
        attacking_dino.attack(attacked_robot)

    def robo_turn(self):
        attacking_robo = self.fleet.robot[0]
        attacked_dino = self.herd.dinosaur[0]
        attacking_robo.attack(attacked_dino)

    def show_dino_opponent_options(self):
        #self.dino_opponent = [Dinosaur]
        pass

    def show_robo_opponent_options(self):
        #self.robo_opponent = [Robot]
        pass

    def display_winners(self):
        pass

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.dino_turn()
        self.robo_turn()
        self.dino_turn()
        self.show_dino_opponent_options()
        self.show_robo_opponent_options()
        self.display_winners()

