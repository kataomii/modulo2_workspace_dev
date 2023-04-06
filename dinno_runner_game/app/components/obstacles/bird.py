from pygame.sprite import Sprite
import random
from app.utils.constants import SCREEN_WIDTH
from app.utils.constants import BIRD

class Bird(Sprite):
    def __init__(self):
        self.index = 0
        self.image = BIRD
        self.rect = self.image[self.index].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = 250 if random.randint(0, 1) else 300
        self.count = 0

    def update(self, obstacles):
        self.animation()
        self.rect.x -= 20
        if self.rect.x < -100:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.index], (self.rect))

    def animation(self):
        if self.count <= 10:
            self.index = 0
        else:
            self.index = 1

        self.count += 1
        if self.count == 20:
            self.count = 0 