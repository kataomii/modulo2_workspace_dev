import pygame
from app.utils.constants import (BG,
                                 ICON, 
                                 SCREEN_HEIGHT, 
                                 SCREEN_WIDTH, 
                                 TITLE, 
                                 FPS, 
                                 BLACK,
                                 CUADRO_ESCALE,
                                 RED,
                                 GREEN,
                                 BLUE,
                                 WHITE,
                                 YELLOW,
                                 BIRD,
                                 LARGE_CACTUS,
                                 RUNNING,
                                 BG_MENU,
                                 MARCO_ESCALE,
                                 FONDO_ESCALE
                                 
)
from app.components.cloud.clouds_random import CloudsRandom
from app.components.sun.sun import Sun
from app.components.dinosaur.dinosaur import Dinosaur
from app.components.obstacles.obstacles_manager import ObstacleManager
from app.components.text.text import Text

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.sun = Sun()
        self.clouds = CloudsRandom()
        self.dinosaur = Dinosaur()
        self.obstacles = ObstacleManager()
        self.text = Text()
        self.music = pygame.mixer.Sound("dinno_runner_game/app/assets/Music/music_game.ogg")
        self.music.play(-1)
        self.music.set_volume(0.2)

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.sun.animation_sun()
        self.clouds.moving_clouds()
        self.dinosaur.update(pygame.key.get_pressed())
        self.obstacles.update(self.dinosaur)
        
    def draw(self):
        self.clock.tick(FPS)
        #self.screen.fill((127,255,212))
        self.screen.blit(FONDO_ESCALE,(0,-370))
        self.draw_background()
        self.sun.draw_sun(self.screen)
        self.clouds.draw_clouds(self.screen)
        self.dinosaur.draw(self.screen)
        self.screen.blit(CUADRO_ESCALE,(0,-40))
        self.screen.blit(MARCO_ESCALE,(SCREEN_WIDTH//2+200,-40))
        self.obstacles.draw(self.screen)
        self.text.draw_text("DINO", 
                            BLACK, 
                            50, 
                            SCREEN_WIDTH//2 - 100, 
                            10, 
                            self.screen
        )
        self.update_game_over()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def update_game_over(self):
        while self.obstacles.game_over:
            self.draw_game_over()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.obstacles.game_over = False
                    self.playing = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.obstacles.game_over = False

    def draw_game_over(self):
        pygame.draw.polygon(self.screen, RED, [[0,0],[0,SCREEN_HEIGHT],[SCREEN_WIDTH//2,SCREEN_HEIGHT//2]])
        pygame.draw.polygon(self.screen, RED, [[0,0],[SCREEN_WIDTH//2,0],[SCREEN_WIDTH//2,SCREEN_HEIGHT//2]])
        pygame.draw.polygon(self.screen, GREEN, [[0,SCREEN_HEIGHT],[SCREEN_WIDTH,SCREEN_HEIGHT],[SCREEN_WIDTH//2,SCREEN_HEIGHT//2]])
        pygame.draw.polygon(self.screen, YELLOW, [[SCREEN_WIDTH,0],[SCREEN_WIDTH,SCREEN_HEIGHT],[SCREEN_WIDTH//2,SCREEN_HEIGHT//2]])
        pygame.draw.circle(self.screen, WHITE, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), 150)
        pygame.draw.circle(self.screen, BLUE, (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), 130)
        pygame.draw.rect(self.screen, WHITE, (0,0 ,SCREEN_WIDTH,SCREEN_HEIGHT), 15)

        self.screen.blit(BG, (SCREEN_WIDTH//2+124, SCREEN_HEIGHT//2 +70) )
        self.screen.blit(BG_MENU, (-60, SCREEN_HEIGHT//2 +70) )
        image_running = pygame.transform.scale(RUNNING[0],(200,200))
        self.screen.blit(image_running, (SCREEN_WIDTH//2-110, SCREEN_HEIGHT//2 - 100))
        image_cactus = pygame.transform.scale(LARGE_CACTUS[2],(200,200))
        self.screen.blit(image_cactus, (SCREEN_WIDTH//2 + 200, SCREEN_HEIGHT//2 - 100))
        self.screen.blit(image_cactus, (150, SCREEN_HEIGHT//2 - 100))
        image_bird = pygame.transform.scale(BIRD[1],(150,150))
        self.screen.blit(image_bird, (SCREEN_WIDTH/2 + 25, 0))

        self.text.draw_text("Press ""space"" to play again",
                            BLACK,
                            30,
                            SCREEN_WIDTH//2 -200,
                            SCREEN_HEIGHT//2 +200,
                            self.screen                    
        )
