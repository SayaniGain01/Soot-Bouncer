import pygame as pg
import sys,time
from soot import Soot
from totoro import Totoro
pg.init()

class Game:
    def __init__(self):
        #setting window config
        self.width = 640
        self.height = 480
        self.scale_factor=0.03
        self.win=pg.display.set_mode((self.width,self.height))
        self.clock=pg.time.Clock()
        self.move_speed=70

        self.jump_sound = pg.mixer.Sound("soundeffects/jump.mp3")
        self.die_sound = pg.mixer.Sound("soundeffects/die.mp3")
        self.score_sound = pg.mixer.Sound("soundeffects/point.mp3")


        self.soot=Soot(self.scale_factor)
        self.is_enter_pressed=False

        self.totoros = []
        self.spawn_timer = 0
        self.spawn_interval = 2.0

        self.is_game_over= False
        self.has_played_die_sound = False


        self.setUpBg()
        self.game_over_img = pg.image.load("images/gameover.png").convert_alpha()
        self.game_over_rect = self.game_over_img.get_rect(center=(self.width // 2, self.height // 2.8))
        self.restart_img = pg.image.load("images/restart.png").convert_alpha()
        self.restart_rect = self.restart_img.get_rect(center=(self.width // 2, self.height // 2))

        self.gameLoop()

    def gameLoop(self):
        last_time=time.time()
        while True:
            #calculating delta time
            new_time = time.time()
            delta_time = new_time-last_time
            last_time = new_time
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        self.is_enter_pressed=True
                    if event.key == pg.K_SPACE and not self.is_game_over:
                        self.soot.flap(delta_time)
                        self.jump_sound.play()
                
                if event.type == pg.MOUSEBUTTONDOWN and self.is_game_over:
                    mouse_pos = pg.mouse.get_pos()
                    if self.restart_rect.collidepoint(mouse_pos):
                        self.resetGame()

            self.updateEverything(delta_time)
            self.checkCollision()
            self.drawEverything()
            pg.display.update()  
            self.clock.tick(60)     #60 frames per sec

    # def check_score(self):

    def resetGame(self):
        self.soot=Soot(self.scale_factor)
        self.is_enter_pressed = True
        self.is_game_over=False
        self.totoros=[]
        self.spawn_timer=0
        self.has_played_die_sound=False


    def checkCollision(self):
        for totoro in self.totoros:
            if self.soot.rect.colliderect(totoro.rect):
                self.is_game_over=True
                if not self.has_played_die_sound:
                    self.die_sound.play()
                    self.has_played_die_sound = True
                return True
            
            if self.soot.rect.bottom>=455:
                self.is_game_over=True
                if not self.has_played_die_sound:
                    self.die_sound.play()
                    self.has_played_die_sound = True
                return True
            if self.soot.rect.top<=0:
                self.is_game_over=True
                if not self.has_played_die_sound:
                    self.die_sound.play()
                    self.has_played_die_sound = True
                return True
            
            return False
            
            
    def updateEverything(self,delta_time):
        if self.is_game_over:
            return

        if self.is_enter_pressed:
            self.bg1_rect.x-=self.move_speed*delta_time
            self.bg2_rect.x-=self.move_speed*delta_time

            if self.bg1_rect.right<0:
                self.bg1_rect.x = self.bg2_rect.right
            elif self.bg2_rect.right<0:
                self.bg2_rect.x = self.bg1_rect.right

            self.soot.update(delta_time)

            self.spawn_timer += delta_time
            if self.spawn_timer >= self.spawn_interval:
                self.spawn_timer = 0
                new_totoro = Totoro()
                self.totoros.append(new_totoro)
# Update all existing Totoros
        for totoro in self.totoros:
            totoro.update(delta_time)
            totoro.rect.x -= self.move_speed * delta_time  # move left
# Remove any that go off screen
        self.totoros = [t for t in self.totoros if not t.rect.right < 0]


    def drawEverything(self):
        self.win.blit(self.bg1_img,self.bg1_rect)
        self.win.blit(self.bg2_img,self.bg2_rect)
        self.win.blit(self.soot.image,self.soot.rect)

        for totoro in self.totoros:
            self.win.blit(totoro.image, totoro.rect)
        
        if self.is_game_over:
            self.win.blit(self.game_over_img,self.game_over_rect)
            self.win.blit(self.restart_img,self.restart_rect)


    def setUpBg(self):
        #laoding images for bg 
        self.bg1_img=pg.transform.scale(pg.image.load("images/bg.png").convert(),(640,480))
        self.bg2_img=pg.transform.scale(pg.image.load("images/bg.png").convert(),(640,480))

        self.bg1_rect=self.bg1_img.get_rect()
        self.bg2_rect=self.bg2_img.get_rect()

        self.bg1_rect.x=0
        self.bg2_rect.x=self.bg1_rect.right
        self.bg1_rect.y=self.bg2_rect.y=0


game = Game()



