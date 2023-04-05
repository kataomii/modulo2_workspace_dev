import pygame
class Text:
    def draw_text(self, text, color, size, x, y, screen):
        font = pygame.font.SysFont("Eras ITC",size)
        text_surface = font.render(text , True, color)
        screen.blit(text_surface, (x,y))