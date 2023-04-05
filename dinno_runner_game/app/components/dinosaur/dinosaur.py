from app.utils.constants import RUNNING, JUMPING, DUCKING
from pygame.sprite import Sprite
import pygame

POS_X = 100
POS_Y = 310
JUMP_VEL = 9

class Dinosaur(Sprite):
    def __init__(self):
        self.index = 0
        self.image = RUNNING[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = POS_X
        self.rect.y = POS_Y
        self.running = False
        self.jumping = False
        self.ducking = False
        self.count = 0
        self.jump_vel = JUMP_VEL

    def draw(self, screen):
        screen.blit(self.image, (self.rect))

    def update(self):
        if self.running:
            self.run()
        elif self.ducking:
            self.duck()
        elif self.jumping:
            self.jump()
        
    def run(self):
        self.image = RUNNING[self.index]
        self.rect.x = POS_X
        self.rect.y = POS_Y
        self.animation() 

    def jump(self):
        self.image = JUMPING
        if self.jumping:                    
            self.rect.y -= self.jump_vel * 4
            self.jump_vel -= 1
        if self.jump_vel < -JUMP_VEL:
            self.rect.y = POS_Y
            self.jumping = False
            self.jump_vel = JUMP_VEL  

    def duck(self):
        self.image = DUCKING[self.index]
        self.rect.y = 350
        self.animation() 

    def animation(self):
        if self.count <= 5:
            self.index = 0
        else:
            self.index = 1

        self.count += 1
        if self.count == 10:
            self.count = 0 
        
    def control(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and not self.jumping:
                self.running = False
                self.ducking = True
                self.jumping = False
            elif event.key == pygame.K_UP and not self.jumping:
                self.running = False
                self.ducking = False
                self.jumping = True
            elif event.key == pygame.K_r and not self.jumping:
                self.running = True
                self.ducking = False
                self.djumping = False

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN and not self.jumping:
                self.running = False
                self.ducking = False
                self.jumping = False
            elif event.key == pygame.K_r:
                self.running = False
                self.ducking = False
                self.djumping = False
        