from app.components.obstacles.cactus import Cactus
from app.utils.constants import SMALL_CACTUS, SCREEN_WIDTH, LARGE_CACTUS, BLACK
import random
from app.components.obstacles.bird import Bird
from app.components.text.text import Text 

class ObstacleManager:
    def __init__(self):
        self.text = Text()
        self.obstacles = []
        self.contador = 0
        self.contador_2 = 0

    def update(self, dinosaur):
        if len(self.obstacles) < 1:
            self.contador += 1
            random_num = random.randint(0,2)
            if random_num == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS,SCREEN_WIDTH,325))
            elif random_num == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS,SCREEN_WIDTH,310))
            elif random_num == 2:
                self.obstacles.append(Bird())
        
        for obstacle in self.obstacles:
            obstacle.update(self.obstacles)
            if dinosaur.rect.colliderect(obstacle.rect):
                self.contador_2 += 1
                
    def draw(self, screen):
        self.text.draw_text(f"obstaculos creados {self.contador}",
                            BLACK,
                            20,
                            10,
                            60,
                            screen                                   
        )
        self.text.draw_text(f"obstaculos chocados {self.contador_2}",
                            BLACK,
                            20,
                            10,
                            100,
                            screen                                   
        )
        for obstacle in self.obstacles:
            obstacle.draw(screen) 