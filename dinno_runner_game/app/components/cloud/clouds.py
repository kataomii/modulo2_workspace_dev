from app.utils.constants import CLOUDS
import pygame

IMAGE_1 = pygame.transform.scale(CLOUDS[0],(130,70))
IMAGE_2 = pygame.transform.scale(CLOUDS[1],(130,70))
CLOUDS_LIST =[IMAGE_1,IMAGE_2]

class Cloud:
    def __init__(self, x, y):
        self.index = 1
        self.pos_cloud_y = y
        self.pos_cloud_x = x
        self.count = 0
    
    def draw_cloud(self, screen):
        screen.blit(CLOUDS_LIST[self.index], (self.pos_cloud_x,self.pos_cloud_y))

    def move_cloud(self, clouds):
        self.animation()
        self.pos_cloud_x -= 5
        if self.pos_cloud_x <= -100:
            clouds.remove(self)
            
    def animation(self):
        if self.count <= 5:
            self.index = 0
        else:
            self.index = 1 

        self.count += 1
        if self.count == 10:
            self.count = 0