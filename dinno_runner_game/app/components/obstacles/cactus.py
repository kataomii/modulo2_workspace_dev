from pygame.sprite import Sprite
from app.utils.constants import SCREEN_WIDTH
import random

class Cactus(Sprite):
    def __init__(self, image, x, y):
        self.random = random.randint(0,2)
        self.image = image[self.random]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, obstacles):
        self.rect.x -= 20
        if self.rect.x < -100:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image, (self.rect))
        
