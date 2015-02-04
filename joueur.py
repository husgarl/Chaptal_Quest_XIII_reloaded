import collision
import math

class Joueur:
    
    def __init__(self):
        self.name = ""
        self.position = ["test",2,2]
    
    #mouvement de x cases vers la droite
    # et de y cases vers le bas
    def mouvement(self,x,y):
        if collision.checkJoueur(self,x,0):
            self.position[1] += x
        if collision.checkJoueur(self,0,y):
            self.position[2] += y
            