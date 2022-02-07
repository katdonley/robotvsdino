
from fleet import Fleet
from herd import Herd



class Battlefield:

    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()
           
    def display_welcome(self):
        print("Welcome to Robots vs. Dinosaurs!")

    def battle(self):
        self.show_robo_opponent_options()
        self.robot_choice = self.fleet.robot[int(input('Enter the number of the robot you want to play: '))]
        self.show_dino_opponent_options()
        self.dino_choice = self.herd.dinosaur[int(input('enter the number of the dinosaur you want to play: '))]
        self.dino_turn()
        self.robo_turn()

    def dino_turn(self):
        attacking_dino = self.herd.dinosaur[0]
        attacked_robot = self.fleet.robot[0]
        attacking_dino.attack(attacked_robot)

    def robo_turn(self):
        attacking_robo = self.fleet.robot[0]
        attacked_dino = self.herd.dinosaur[0]
        attacking_robo.attack(attacked_dino)
        self.herd.dinoasur.health -= int(self.fleet.robot.weapon.attack_power)

    def show_dino_opponent_options(self):
        dino_counter = 0
        for dinosaur in self.herd.dinosaur:
            print(f'{dino_counter}, {dinosaur.name}')
            dino_counter += 1

    def show_robo_opponent_options(self):
        robo_counter = 0
        for robot in self.fleet.robot:
            print(f'{robo_counter}, {robot.name}')
            robo_counter += 1

    def show_robo_weapon_options(self):
        robo_weapon_counter = 0
        for weapon in self.fleet.robot.weapon.name:
            print(f'{robo_weapon_counter}')

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

#robot.health == 100
        #robot.health -= self.attack_power
        #print(f'The robot {robot.name} was hit ')