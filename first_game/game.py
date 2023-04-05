import pygame

COLOR_RED = (255, 0, 0)
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.ball_speed = [10, 10]
        self.ball = pygame.draw.circle(
            surface=self.screen, color=COLOR_RED, center=[100, 100], radius=40)

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

    def update(self):
        pass

    def draw(self):
        self.clock.tick(30)
        self.screen.fill((255, 255, 255))
        self.move_ball()
        pygame.display.update()
        pygame.display.flip()

    def move_ball(self):
        print(f"moving ballon with {self.ball_speed}")
        self.ball = self.ball.move(self.ball_speed)
        if self.ball.left <= 0 or self.ball.right >= 600:
            self.ball_speed[0] = -self.ball_speed[0]
        if self.ball.top <= 0 or self.ball.bottom >= 600:
            self.ball_speed[1] = -self.ball_speed[1]
        self.ball = pygame.draw.circle(
            surface=self.screen, color=COLOR_RED, center=self.ball.center, radius=40)
