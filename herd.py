from dinosaur import Dinosaur


class Herd:

    def __init__(self):
        self.dinosaur = [Dinosaur("Ralph", 50, 100), Dinosaur("Paul", 40, 100), Dinosaur("Chuck", 30, 100)]
        
    def create_herd(self, select_dino):
        self.select_dino = input("Choose your dino: ")


    