import random
from app.components.cloud.clouds import Cloud

class CloudsRandom:
    def __init__(self):
        self.clouds = []

    #def new_clouds(self):
        #pos_x = (random.randint(1100,1400))
        #pos_y = (random.randint(0, 150))
        #nube = Cloud(pos_x, pos_y)
        #self.clouds.append(nube)

    def moving_clouds(self):
        while len(self.clouds) < 5:
            pos_x = (random.randint(1100,1800))
            pos_y = (random.randint(0, 110))
            nube = Cloud(pos_x, pos_y)
            self.clouds.append(nube)

        for nube in self.clouds:
            nube.move_cloud(self.clouds)

    def draw_clouds(self, screen):
        for nube in self.clouds:
            nube.draw_cloud(screen)
