

class Dinosaur:

    def __init__(self, name, attack_power, health):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        

    def attack(self, robot):
        robot.health -= self.attack_power
        print(f'The robots name is {robot.name}')