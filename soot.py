import pygame as pg

class Soot(pg.sprite.Sprite):
    def __init__(self,scale_factor):
        super().__init__()
        self.image = pg.transform.scale_by(pg.image.load("images/sootsprite.png").convert_alpha(),scale_factor)
        self.rect = self.image.get_rect(center=(200,300))
        self.y_velocity=0
        self.gravity=10
        self.flap_speed = 250
    
    def update(self,delta_time):
        self.applyGravity(delta_time)

        if self.rect.y<=0 and self.flap_speed==250:
            self.rect.y=0
            self.flap_speed=0
            self.y_velocity=0
        elif self.rect.y>0 and self.flap_speed==0:
            self.flap_speed=250
            

    def applyGravity(self,delta_time):
        self.y_velocity+=self.gravity*delta_time
        self.rect.y+= self.y_velocity

    def flap(self,delta_time):
        self.y_velocity=-self.flap_speed*delta_time
