import collision
import math

class Joueur:
    
    def __init__(self,x,y):
        self.name       = ""
        self.position   = ["base",x,y]
        self.hitbox     = [ -1/4 , 1/4 , -1/4 , 1/4 ]  # xmin , xmax , ymin , ymax
        self.spriteName = "gobelin"
        self.direction  = 1
    
    #mouvement de x cases vers la droite
    # et de y cases vers le bas
    def mouvement(self,x,y):
        if x> 0:
            self.direction = 4
        elif x< 0:
            self.direction = 8
        elif y> 0:
            self.direction = 2
        elif y< 0:
            self.direction = 6
        else:
            if self.direction % 2 == 0:
                self.direction -= 1
            
        if collision.checkJoueur(self,x,0):
            self.position[1] += x
        if collision.checkJoueur(self,0,y):
            self.position[2] += y
            