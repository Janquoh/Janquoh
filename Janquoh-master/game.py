import pygame, levels

class Player(object):
    def __init__(self,x,y):
        self.rect = pygame.Rect(x, y, 25, 25)
        self.velocityX = 0
        self.velocityY = 0
        self.velocityMax = 10
        self.acceletarion = 0.2
        self.DeAcceletarion = 0.1

    def Controls(self, walls):
        key = pygame.key.get_pressed()

        if key[pygame.K_UP] and key[pygame.K_RIGHT]:
            if self.velocityY > -self.velocityMax*0.78: self.velocityY -= self.acceletarion
            if self.velocityX < self.velocityMax: self.velocityX += self.acceletarion
        elif key[pygame.K_RIGHT] and key[pygame.K_DOWN]:
            if self.velocityX < self.velocityMax: self.velocityX += self.acceletarion
            if self.velocityY < self.velocityMax: self.velocityY += self.acceletarion
        elif key[pygame.K_DOWN] and key[pygame.K_LEFT]:
            if self.velocityY < self.velocityMax: self.velocityY += self.acceletarion
            if self.velocityX > -self.velocityMax*0.78: self.velocityX -= self.acceletarion
        elif key[pygame.K_UP] and key[pygame.K_LEFT]:
            if self.velocityY > -self.velocityMax*0.78: self.velocityY -= self.acceletarion
            if self.velocityX > -self.velocityMax*0.78: self.velocityX -= self.acceletarion
        elif key[pygame.K_UP]:
            if self.velocityY > -self.velocityMax*0.78: self.velocityY -= self.acceletarion
        elif key[pygame.K_RIGHT]:
            if self.velocityX < self.velocityMax: self.velocityX += self.acceletarion
        elif key[pygame.K_DOWN]:
            if self.velocityY < self.velocityMax: self.velocityY += self.acceletarion
        elif key[pygame.K_LEFT]:
            if self.velocityX > -self.velocityMax*0.78: self.velocityX -= self.acceletarion

        if self.velocityX > 0: self.velocityX -= self.DeAcceletarion
        if self.velocityX < 0: self.velocityX += self.DeAcceletarion

        if self.velocityY > 0: self.velocityY -= self.DeAcceletarion
        if self.velocityY < 0: self.velocityY += self.DeAcceletarion

        if self.velocityX != 0: self.move_single_axis(self.velocityX, 0, walls)
        if self.velocityY != 0: self.move_single_axis(0, self.velocityY, walls)

    def move_single_axis(self, x, y, walls):

        self.rect.x += x
        self.rect.y += y


        for wall in walls:
            if self.rect.colliderect(wall.rect) and wall.type == 1:
                if x > 0:
                    self.rect.right = wall.rect.left
                    self.velocityX = 0
                if x < 0:
                    self.rect.left = wall.rect.right
                    self.velocityX = 0
                if y > 0:
                    self.rect.bottom = wall.rect.top
                    self.velocityY = 0
                if y < 0:
                    self.rect.top = wall.rect.bottom
                    self.velocityY = 0

class Bullet(object):
    def __init__(self, playerPos):
        self.point=playerPos
        #self.direction=mousePosition
        self.rect=pygame.Rect(self.point[0], self.point[1], 5,15)
        self.image=pygame.image.load("Assets/sprite.png")
        #self.speed=moveSpeed
        self.surface=pygame.Surface((5,15))
        self.surface.fill((123,12,123))
class Wall(object):
    def __init__(self, pos, list, type, level, side):
        list.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 25, 25)
        self.type = type
        self.level = level
        self.side = side

def LoadLevel(level):

    walls = []
    x = y = 0

    for row in level:
        for col in row:
            if col == "a":
                Wall((x, y), walls, 1, 0, 0)
            if col == "b":
                Wall((x, y), walls, 2, levels.Lvl2(), 2)
            if col == "c":
                Wall((x, y), walls, 2, levels.Lvl1(), 4)
            if col == "d":
                Wall((x, y), walls, 2, levels.Lvl3(), 3)
            if col == "e":
                Wall((x, y), walls, 2, levels.Lvl2(), 1)
            if col == "f":
                Wall((x, y), walls, 2, levels.Lvl4(), 4)
            if col == "g":
                Wall((x, y), walls, 2, levels.Lvl3(), 2)
            if col == "h":
                Wall((x, y), walls, 2, levels.Lvl1(), 1)
            if col == "i":
                Wall((x, y), walls, 2, levels.Lvl4(), 3)
            x += 25
        y += 25
        x = 0
    return walls

def LoadLevelNew(level):

    walls = []
    x = y = 0

    for row in level:
        for col in row:
            print(col)
            if col == "a":
                Wall((x, y), walls, 1, 0, 0)
            if col == "d1adasdasd":
                Wall((x, y), walls, 1, 0, 0)
            x += 25
        y += 25
        x = 0
    return walls
