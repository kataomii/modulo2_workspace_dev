import pygame
from app.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, BLACK
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
            self.dinosaur.control(event)

    def update(self):
        self.sun.animation_sun()
        self.clouds.moving_clouds()
        self.dinosaur.update()
        self.obstacles.update(self.dinosaur)
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((127,255,212))
        self.draw_background()
        self.sun.draw_sun(self.screen)
        self.clouds.draw_clouds(self.screen)
        self.dinosaur.draw(self.screen)
        self.obstacles.draw(self.screen)
        self.text.draw_text("DINO", BLACK, 50, 10, 10, self.screen)
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
    