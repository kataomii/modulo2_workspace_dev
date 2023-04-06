from app.components.obstacles.cactus import Cactus
from app.utils.constants import SMALL_CACTUS, SCREEN_WIDTH, LARGE_CACTUS, BLACK, BIRD
import random
from app.components.obstacles.bird import Bird
from app.components.text.text import Text 
import pygame

CACTUS_ESCALE = pygame.transform.scale(LARGE_CACTUS[2], (40,40))
BIRD_ESCALE = pygame.transform.scale(BIRD[1], (40,40))

class ObstacleManager:
    def __init__(self):
        self.text = Text()
        self.obstacles = []
        self.count_Cactus = 0
        self.count_Collide = 0
        self.count_bird = 0
        self.collide = False
        self.cactus = False
        self.birds = False
        self.points = 0
        self.game_over = False

    def update(self, dinosaur):
        self.game_reset()
        if len(self.obstacles) < 1:
            random_num = random.randint(0,2)
            if random_num == 0:
                self.count_Cactus += 1
                self.cactus = True
                self.birds = False
                self.obstacles.append(Cactus(SMALL_CACTUS,SCREEN_WIDTH,325))
            elif random_num == 1:
                self.count_Cactus += 1
                self.cactus = True
                self.birds = False
                self.obstacles.append(Cactus(LARGE_CACTUS,SCREEN_WIDTH,310))
            elif random_num == 2:
                self.count_bird += 1
                self.birds = True
                self.cactus = False
                self.obstacles.append(Bird())
        
        for obstacle in self.obstacles:
            obstacle.update(self.obstacles)
            if dinosaur.rect.colliderect(obstacle.rect) and not self.collide:
                self.count_Collide += 1
                self.collide = True
                if self.cactus:
                    self.points -= 50
                if self.birds:
                    self.points -= 25
            if not dinosaur.rect.colliderect(obstacle.rect):
                self.collide = False
                if obstacle.rect.x == dinosaur.rect.x:
                    if self.cactus:
                        self.points += 100
                    if self.birds:
                        self.points += 75
                
                
    def draw(self, screen):
        self.text.draw_text(f"CACTUS {self.count_Cactus}",
                            BLACK,
                            20,
                            120,
                            34,
                            screen                                   
        )
        screen.blit(CACTUS_ESCALE,(50,20))
        self.text.draw_text(f"BIRS {self.count_bird}",
                            BLACK,
                            20,
                            120,
                            78,
                            screen                                   
        )
        screen.blit(BIRD_ESCALE,(50,60))
        self.text.draw_text(f"crashed obstacles {self.count_Collide}",
                            BLACK,
                            20,
                            50,
                            110,
                            screen                                   
        )
        self.text.draw_text(f"SCORE {self.points}",
                            BLACK,
                            20,
                            800,
                            30,
                            screen                                   
        )
        
        for obstacle in self.obstacles:
            obstacle.draw(screen) 
        
    def game_reset(self):
        if self.points <= -100:
            self.game_over = True
            self.obstacles = []
            self.count_Cactus = 0
            self.count_Collide = 0
            self.count_bird = 0
            self.collide = False
            self.cactus = False
            self.birds = False
            self.points = 0