from weapon import Weapon



class Robot:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.weapon = [Weapon("sword", 30), Weapon("axe", 30), Weapon("pitchfork", 30)]
        
        
    def attack(self, dinosaur):
         
        weapon_counter = 0
        for weapon in self.weapon:
            print(f'{weapon_counter}, with attack power {weapon.attack_power}')
            weapon_counter += 1
            print(f'The robot {self.name} attacked the dinosaur {dinosaur} with a {self.weapon}')
            


    
    