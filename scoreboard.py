import pygame as pg

class Scoreboard:
    def __init__(self, font_size=40, position=(20,20), font_path="pixel_font.ttf",screen_width=640):
        self.score=0
        self.high_score = 0
        self.font = pg.font.Font(font_path, font_size)
        self.position = position
        self.color = (0,0,0)
        self.screen_width = screen_width

    def increase(self):
        self.score+=1
        if self.score> self.high_score:
            self.high_score=self.score

    def reset(self):
        self.score=0
    
    def draw(self,surface):
        # Main score (top-left)
        score_text = self.font.render(f"Score: {self.score}", False, self.color)
        surface.blit(score_text, self.position)

        # High score (top-right)
        high_text = self.font.render(f"High: {self.high_score}", False, self.color)
        high_rect = high_text.get_rect(topright=(self.screen_width - 20, self.position[1]))
        surface.blit(high_text, high_rect.topleft)
