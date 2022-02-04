from weapon import Weapon
import random


class Robot:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = Weapon

    def attack(self, dinosaur):
        dinosaur.health -= int(self.weapon.attack_power)
        print(f'The dinosaurs name is {dinosaur.name}')


    
    