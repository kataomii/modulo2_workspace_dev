import pygame
from app.utils.constants import SCREEN_WIDTH, SUNS

IMAGE_1 = pygame.transform.scale(SUNS[0],(200,180))
IMAGE_2 = pygame.transform.scale(SUNS[1],(200,180))
SUNS_LIST =[IMAGE_1,IMAGE_2]

class Sun:
    def __init__(self):
        self.index = 0
        self.pos_x = SCREEN_WIDTH
        self.pos_y = 0
        self.count = 0

    def draw_sun(self, screen):
        screen.blit(SUNS_LIST[self.index], (self.pos_x-150,self.pos_y))
    
    def animation_sun(self):
        if self.count <= 5:
            self.index = 0
        else:
            self.index = 1

        self.count += 1
        if self.count == 10:
            self.count = 0 