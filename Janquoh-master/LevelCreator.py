import pygame
from os import environ

"""
# state 1 = Eraser
# state 2 = Wall
# state 3 = Make Border
# state 4 = Clean Field
# state 5 = Make Door
# state 6 = Point
# state 7 = Export

clipboard
"""

class Creator(object):
    def __init__(self, x, y, id):
        self.id = id
        self.rect = pygame.Rect(x, y, 25, 25)
        self.state = 1
        self.dir = 0

    def Action(self,current, event, maps, position):
        if event.type != pygame.KEYDOWN and event.type != pygame.KEYUP:
            if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(event.pos):
                if current == 2 or current == 1:
                    self.state = current
                for x in range(34):
                    if current == 5 and self.id == x+3:
                        maps[array[position[0]-1][position[1]]][x + 952].state = current
                        maps[array[position[0] - 1][position[1]]][x + 952].dir = 2
                        self.state = current
                        self.dir = 1
                    if current == 5 and self.id == x + 953:
                        maps[array[position[0]+1][position[1]]][x - 986].state = current
                        maps[array[position[0] + 1][position[1]]][x - 986].dir = 1
                        self.state = current
                        self.dir = 2
                for x in range(22):
                    if current == 5 and self.id == (x+3)*38 - 37:
                        maps[array[position[0]][position[1] - 1]][(x + 3) * 38 - 1].state = current
                        maps[array[position[0]][position[1] - 1]][(x + 3) * 38 - 1].dir = 4
                        self.state = current
                        self.dir = 3
                    if current == 5 and self.id == (x + 3) * 38:
                        maps[array[position[0]][position[1]+1]][(x + 3) * 38 - 38].state = current
                        maps[array[position[0]][position[1] + 1]][(x + 3) * 38 - 38].dir = 3
                        self.state = current
                        self.dir = 4
                print("tiler:", self.id, " /// state:" , self.state)

class Tool(object):
    def __init__(self, x, y, id):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.id = id

    def Click(self, current, event, maps, position):
        if self.rect.collidepoint(event.pos):
            if self.id == 1 or self.id == 2:
                current = self.id
            if self.id == 3:
                for x in range(38):
                    if maps[array[position[0]][position[1]]][x].state != 5:
                        maps[array[position[0]][position[1]]][x].state = 2
                    if maps[array[position[0]][position[1]]][x+950].state != 5:
                        maps[array[position[0]][position[1]]][x+950].state = 2
                for x in range(26):
                    if maps[array[position[0]][position[1]]][x].state != 5:
                        if maps[array[position[0]][position[1]]][x*38].state != 5:
                            maps[array[position[0]][position[1]]][x*38].state = 2
                        if maps[array[position[0]][position[1]]][x * 38 - 1].state != 5:
                            maps[array[position[0]][position[1]]][x * 38 - 1].state = 2
            if self.id == 4:
                for map in maps[array[position[0]][position[1]]]:
                    map.state = 1
            if self.id == 5 or self.id == 6:
                current = self.id
            if self.id == 7:
                print("WIP Exporting")
                Export(maps)

            print("clicking in tool:", self.id, " /// state:", self.id)
        return current, maps

class Button(object):
    def __init__(self, rect, id):
        self.rect = pygame.Rect(rect)
        self.id = id

    def Click(self, event, maps, position, miniMap):
        if event.type != pygame.KEYDOWN and event.type != pygame.KEYUP:
            if self.rect.collidepoint(event.pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if self.id == 1 and position[1]!=7:
                    HardUpdate(position, maps[array[position[0]][position[1]]], miniMap)
                    position[1] += 1
                elif self.id == 2 and position[1]!=0:
                    HardUpdate(position, maps[array[position[0]][position[1]]], miniMap)
                    position[1] -= 1
                elif self.id == 3 and position[0]!=0:
                    HardUpdate(position, maps[array[position[0]][position[1]]], miniMap)
                    position[0] -= 1
                elif self.id == 4 and position[0]!=7:
                    HardUpdate(position, maps[array[position[0]][position[1]]], miniMap)
                    position[0] += 1
        return position

class MiniMap(object):
    def __init__(self, x, y, id):
        self.x, self.y = y, x
        self.rect = pygame.Rect(x * 36 + 1005, y * 24 + 20, 34, 22)
        self.state = 0
        self.id = id
        self.hard = []

    def Click(self, event, position, maps, miniMap):
        if event.type != pygame.KEYDOWN and event.type != pygame.KEYUP:
            if self.rect.collidepoint(event.pos) and event.type == pygame.MOUSEBUTTONDOWN:

                HardUpdate(position, maps[array[position[0]][position[1]]], miniMap)
                position[0] = self.x
                position[1] = self.y
                print(array[position[0]][position[1]])
        return position

def Export(maps):
    ## WIP
    f = open("levels.py", "w+")

    for y in range(8):
        for x in range(8):
            f.write("def Lvl" + str(array[y][x]) + "():\n\treturn [")
            z = 1
            for map in maps[array[x][y]]:
                if z == 1:
                    f.write("[")
                if map.state == 1:
                    f.write("'"+" "+"'")
                elif map.state == 2:
                    f.write("'"+"a"+"'")
                elif map.state == 5: #1 - UP /// 2 - DOWN /// 3 - LEFT /// 4 - RIGHT

                    if map.dir == 1:
                        f.write("'" + str(map.dir) + str(array[y][x-1]) + "'")
                        print("lvl",array[y][x],"// 1 // up", array[y][x-1])
                    if map.dir == 2:
                        f.write("'" + str(map.dir) + str(array[y][x+1]) + "'")
                        print("lvl", array[y][x], "// 2 // down", array[y][x+1])

                    if map.dir == 3:
                        f.write("'" + str(map.dir) + str(array[y-1][x]) + "'")
                        print("lvl", array[y][x], "// 3 // left", array[y-1][x])

                    if map.dir == 4:
                        f.write("'" + str(map.dir) + str(array[y + 1][x]) + "'")
                        print("lvl", array[y][x], "// 4 // right", array[y + 1][x])


                if z < 38:
                    f.write(",")
                z += 1
                if z > 38:
                    z = 1
                    f.write("]")
                    if map.id < 980:
                        f.write(",")
            f.write("]\n\n")
    return [[1,2],[3,4],]

    """
    for map in maps:
        if map.state == 1:
            map.state = ' '
        elif map.state == 2:
            map.state = 'a'
        elif map.state == 5:
            map.state = str(map.dir)
    """
    f.close()

    """
      if map.dir == 1:
          f.write("'"+str(map.dir)+str(array[x][y-1])+"'")
      if map.dir == 3:
          f.write("'"+str(map.dir)+str(array[x][y+1])+"'")
          print("3333333 - E", array[x][y] , " - ",array[x][y - 1])
      if map.dir == 2:
          f.write("'"+str(map.dir)+str(array[x-1][y])+"'")
          print("22222222", array[x + 1][y])
      if map.dir == 4:
          f.write("'"+str(map.dir)+str(array[x+1][y])+"'")
          print("4444444 - D", array[x+1][y])
      print(array[x][y])
      """

    """
    z = -1
    for y in range(len(file)):
        for x in range(len(file[0])):
            z += 1
            file[y][x] = maps[z].state
    """
    """
    for y in range(len(file)):
        for x in range(len(file[0])):
            print("printing :", y, ".", x, "- {", file[y][x], "}")
    """

def EventHandler(current, maps, tools, buttons, position, miniMap):
    for event in pygame.event.get():

        for map in maps[array[position[0]][position[1]]]:
            map.Action(current, event, maps, position)

        if pygame.mouse.get_pressed()[0] and event.type != pygame.KEYDOWN and event.type != pygame.KEYUP:
            for tool in tools:
                current, maps = tool.Click(current, event, maps, position)

            for button in buttons:
                position = button.Click(event, maps, position, miniMap)

            for mini in miniMap:
                position = mini.Click(event, position, maps, miniMap)

        if event.type == pygame.QUIT:
            exit(0)
    return current, position

def HardUpdate(position, maps, miniMap):
    hard = []
    rect = miniMap[array[position[1]][position[0]]].rect
    for map in maps:
        if map.state == 2:
            hard += [pygame.Rect(rect.x+map.rect.x/25-3, rect.y+map.rect.y/25-3,1,1)]
    miniMap[array[position[1]][position[0]]].hard = hard
    return miniMap

def Draw(maps, tools, buttons, current, position, miniMap):
    for map in maps[array[position[0]][position[1]]]:
        if map.state == 2:
            pygame.draw.rect(screen, (100, 100, 100), map.rect, 0)
        elif map.state == 5:
            pygame.draw.rect(screen, (255, 255, 255), map.rect, 0)
            font = pygame.font.SysFont("Arial", 22)
            for x in range(34):
                if map.id == x+3:
                    surface = font.render("↑", True, pygame.Color(200,100,25))
                    screen.blit(surface, (map.rect.x + 7, map.rect.y - 2))
                if map.id == x+953:
                    surface = font.render("↓", True, pygame.Color(200, 100, 25))
                    screen.blit(surface, (map.rect.x + 7, map.rect.y - 2))
            for x in range(22):
                if map.id == (x+3)*38:
                    surface = font.render("→", True, pygame.Color(200, 100, 25))
                    screen.blit(surface, (map.rect.x, map.rect.y - 2))
                if map.id == (x+3)*38 - 37:
                    surface = font.render("←", True, pygame.Color(200,100,25))
                    screen.blit(surface, (map.rect.x, map.rect.y - 2))


        pygame.draw.rect(screen, (200, 200, 200), map.rect, 1)

    for button in buttons:
        pygame.draw.rect(screen, (200, 200, 100), button.rect, 1)

    for mini in miniMap:
        if mini.id == array[position[0]][position[1]]:
            pygame.draw.rect(screen, (25, 200, 175), mini.rect, 0)
        else:
            pygame.draw.rect(screen, (255, 100, 100), mini.rect, 0)

    for tool in tools:
        if tool.id == 1:
            screen.blit(pygame.image.load("Assets/eraser.png"), (tool.rect))
        elif tool.id == 2:
            screen.blit(pygame.image.load("Assets/wall.png"), (tool.rect))
        elif tool.id == 3:
            screen.blit(pygame.image.load("Assets/border.png"), (tool.rect))
        elif tool.id == 4:
            screen.blit(pygame.image.load("Assets/delete.png"), (tool.rect))
        elif tool.id == 5:
            screen.blit(pygame.image.load("Assets/door.png"), (tool.rect))
        elif tool.id == 6:
            screen.blit(pygame.image.load("Assets/wip.png"), (tool.rect))
        elif tool.id == 7:
            screen.blit(pygame.image.load("Assets/wip.png"), (tool.rect))
        else:
            screen.blit(pygame.image.load("Assets/blank.png"), (tool.rect))

        pygame.draw.rect(screen, (100, 100, 100), tool.rect, 1)

    for tool in tools:
        if tool.id == current:
            pygame.draw.rect(screen, (200, 200, 0), tool.rect, 4)

    for mini in miniMap:
        for hard in mini.hard:
            pygame.draw.rect(screen, (200,200,200), hard, 0)

def Create(maps, tools):
    id = 0
    if tools == []:
        x = 1000
        y = 225
        for row in range(8):
            for col in range(4):
                id += 1
                x += 50
                tools += [Tool(x, y, id)]

            y += 50
            x = 1000
        return tools

    if maps == []:
        x = y = 25
        for row in range(26):
            for col in range(38):
                id += 1
                maps += [Creator(x, y, id)]
                x += 25
            y += 25
            x = 25
        return maps

def Main():
    current = 6
    position = [0, 0]

    World = []

    for x in range(100):
        map = []
        map = Create(map, 0)
        World += [map]

    tools = []
    buttons = []

    buttons += [Button((25, 5, 950, 15), 3)]
    buttons += [Button((25, 680, 950,15), 4)]

    buttons += [Button((5, 25, 15, 650), 2)]
    buttons += [Button((980, 25, 15, 650), 1)]

    tools = Create(0, tools)

    miniMap = []

    for x in range(8):
        for y in range(8):
            miniMap += [MiniMap(x,y, array[y][x])]

    while True:

        screen.fill((0, 0, 0))

        Draw(World, tools, buttons, current, position, miniMap)
        current, position = EventHandler(current, World, tools, buttons, position, miniMap)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    pygame.init()

    array = []

    id = 0
    for y in range(8):
        col = []
        for x in range(8):
            col +=[id]
            id += 1
        array += [col]

    environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (30, 25)
    pygame.display.set_caption("Game")
    screen = pygame.display.set_mode((1300, 700))

    clock = pygame.time.Clock()
    Main()
