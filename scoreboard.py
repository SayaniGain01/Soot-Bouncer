import pygame as pg

class Scoreboard:
    def __init__(self, font_size=40, position=(10,10)):
        self.score=0
        self.font = pg.font.Font(None, font_size)
        self.position = position
        self.color = (255,255,255)

    def increase(self):
        self.score+=1

    def reset(self):
        self.score=0
    
    def draw(self,surface):
        text = self.font.render(f"Score:{self.score}", True, self.color)
        surface.blit(text,self.position)