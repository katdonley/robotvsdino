from weapon import Weapon



class Robot:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon_type = [Weapon("sword", 50), Weapon("axe", 40), Weapon("pitchfork", 30)] 
        
    def attack(self, dinosaur):
        dinosaur.health -= int(self.weapon.attack_power)
        print(f'The dinosaurs name is {dinosaur.name}')


    
    