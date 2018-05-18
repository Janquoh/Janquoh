import pygame
class heartContainers(object):
    def __init__(self,x):
        self.state=1
        if self.state==1:
            self.image = pygame.image.load("assets/Heart.png")
        else:self.image = pygame.image.load("assets/deadHeart.png")
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = (x, 15)
class characterPortrait(object):
    def __init__(self):
        self.image = pygame.image.load("assets/player.png")
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = (15, 15)
class miniMap(object):
    def __init__(self):0

class skillMap(object):
    def __init__(self,screen,y,coolDown,assetString):
        self.image=pygame.image.load(assetString)
        self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.center = (25, y)
        self.cd=coolDown
        self.duration=0
class pauseMenu(object):
    def __init__(self):0