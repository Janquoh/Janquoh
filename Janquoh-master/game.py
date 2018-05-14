import pygame, math, levels

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.charge = 10
        self.imageMaster = pygame.image.load("player.png")
        self.imageMaster.convert()
        self.rect = self.imageMaster.get_rect()
        self.rect.center = (320, 240)
        self.dir = 0
        transColor = self.imageMaster.get_at((1, 1))
        self.imageMaster.set_colorkey(transColor)
        self.velocityX = 0
        self.velocityY = 0
        self.velocityMax = 5
        self.acceletarion = 0.2
        self.deAcceletarion = 0.1
        self.bullets = []

        self.hitBox = pygame.Rect(self.rect.x, self.rect.y, 25, 25)

    def Controls(self, walls):
        #self.rect = pygame.Rect(self.rect.x, self.rect.y, 25, 25)
        #self.rect.size[1] = 25
        def move_single_axis(x, y, walls):

            self.hitBox.x += x
            self.hitBox.y += y

            for wall in walls:
                if self.hitBox.colliderect(wall.rect) and wall.type == 1:
                    if x > 0:
                        self.hitBox.right = wall.rect.left
                        self.velocityX = 0
                    if x < 0:
                        self.hitBox.left = wall.rect.right
                        self.velocityX = 0
                    if y > 0:
                        self.hitBox.bottom = wall.rect.top
                        self.velocityY = 0
                    if y < 0:
                        self.hitBox.top = wall.rect.bottom
                        self.velocityY = 0

        if pygame.mouse.get_pressed()[0]:
            shell = Shell(self.rect)
            shell.x = self.rect.centerx
            shell.y = self.rect.centery
            shell.dir = self.dir
            shell.speed = self.charge
            self.bullets += [shell]

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

        if self.velocityX > 0: self.velocityX -= self.deAcceletarion
        if self.velocityX < 0: self.velocityX += self.deAcceletarion

        if self.velocityY > 0: self.velocityY -= self.deAcceletarion
        if self.velocityY < 0: self.velocityY += self.deAcceletarion

        if self.velocityX != 0: move_single_axis(self.velocityX, 0, walls)
        if self.velocityY != 0: move_single_axis(0, self.velocityY, walls)

    def Update(self):
        oldCenter = self.rect.center
        self.image = pygame.transform.rotate(self.imageMaster, self.dir)
        self.rect = self.image.get_rect()
        self.rect.center = oldCenter

        (mousex, mousey) = pygame.mouse.get_pos()
        dx = self.rect.centerx - mousex
        dy = self.rect.centery - mousey
        dy *= -1
        radians = math.atan2(dy, dx)
        self.dir = (radians * 180 / math.pi) + 180
        self.distance = math.sqrt((dx * dx) + (dy * dy))

        #self.rect.x, self.rect.y = self.hitBox.x, self.hitBox.y
        self.rect.center = self.hitBox.center

class Shell(pygame.sprite.Sprite):
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("assets/bullet.png")
        self.image.convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey(self.image.get_at((1, 1)))
        self.speed = 20
        self.dir = 0

        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - player.x, mouse_y - player.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)

        self.image = pygame.transform.rotate(self.image, angle+180)

    def Update(self):
        radians = self.dir * math.pi / 180
        self.dx = math.cos(radians) * self.speed
        self.dy = math.sin(radians) * self.speed
        self.dy *= -1

        self.x += self.dx
        self.y += self.dy

        self.rect.center = (self.x, self.y)


    # DELETE
    """
    def checkKeys(self, screen):
        if self.x > screen.get_width() or self.x < 0 or self.y > screen.get_height() or self.y < 0:
            self.__del__()

    def __del__(self):
        del self
    """

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
