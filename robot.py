from weapon import Weapon



class Robot:

    def __init__(self, name, health):
        self.name = name
        self.health = health
        
        
    def attack(self, dinosaur):
        
        weapon_counter = 0
        for weapon in self.weapon:
            self.weapon = [Weapon("sword", 50), Weapon("axe", 40), Weapon("pitchfork", 30)] 
            print(f'The robot {self.name} attacked the dinosaur {dinosaur} with a {self.weapon_type}')
            weapon_counter += 1


    
    