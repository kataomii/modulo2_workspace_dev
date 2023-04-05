import pygame
class Text:
    def draw_text(self, text, color, size, x, y, screen):
        font = pygame.font.SysFont("Eras ITC",size)
        text_render = font.render(text , True, color)
        screen.blit(text_render, (x,y))