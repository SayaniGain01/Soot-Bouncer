import pygame as pg
import random

class Totoro:
    def __init__(self):
        scale_factor = 0.07
        self.img_big = pg.transform.scale_by(pg.image.load("images/bluetotoro.png").convert_alpha(), scale_factor)
        self.img_small = pg.transform.scale_by(pg.image.load("images/whitetotoro.png").convert_alpha(), scale_factor)


        self.image = random.choice([self.img_big, self.img_small])
        self.rect = self.image.get_rect()

        self.rect.x = 100 + random.randint(0,400)

        self.start_y = 480 + 50  # below screen
        self.target_y = 480 - self.rect.height  # where to pop up

        self.rect.y = self.start_y

        self.state = "rising"
        self.rise_speed = 600
        self.descend_speed = 600
        self.wait_duration = 1.0
        self.wait_timer = 0.0

    def update(self, delta_time):   
        if self.state == "rising":
            self.rect.y -= self.rise_speed * delta_time
            if self.rect.y <= self.target_y:
                self.rect.y = self.target_y
                self.state = "waiting"
                self.wait_timer = self.wait_duration

        elif self.state == "waiting":
            self.wait_timer -= delta_time
            if self.wait_timer <= 0:
                self.state = "descending"

        elif self.state == "descending":
            self.rect.y += self.descend_speed * delta_time

    def is_off_screen(self):
        return self.rect.top > 480



       


  

