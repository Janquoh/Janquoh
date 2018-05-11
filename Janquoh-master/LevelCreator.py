import pygame

"""
# state 1 = Eraser
# state 2 = Wall


clipboard
"""


class Creator(object):
    def __init__(self, x, y, id):
        self.id = id
        self.rect = pygame.Rect(x, y, 25, 25)
        self.state = 0

class Tool(object):
    def __init__(self, x, y, id, state):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.id = id
        self.state = state

class Button(object):
    def __init__(self, x, y, id):
        self.rect = pygame.Rect(x, y, 200, 50)

def Export(maps):
    file = [[" " for x in range(38)] for y in range(26)]

    z = -1
    for y in range(len(file)):
        for x in range(len(file[0])):
            z += 1
            file[y][x] = maps[z].state


    for y in range(len(file)):
        for x in range(len(file[0])):
            print("printing :", y, ".", x, "- {", file[y][x], "}")

    print(file)

def Main():
    running = True

    maps = []
    tools = []
    buttons = []

    x = 1000
    y = 25
    id = 0

    buttons += [Button(1050, 475, 1)]

    for row in range(8):
        for col in range(4):
            id+=1
            x += 50
            if id == 1:
                tools += [Tool(x, y, id, 1)]
            elif id == 2:
                tools += [Tool(x, y, id, 2)]
            else:
                tools += [Tool(x, y, id, 0)]

        y+=50
        x=1000

    id = 0
    x = y = 25

    for row in range(26):
        for col in range(38):
            id+=1
            maps += [Creator(x,y,id)]
            x+=25
        y+=25
        x=25

    current = 0

    while running:
        screen.fill((0, 0, 0))

        for map in maps:
            if map.state == 2:
                pygame.draw.rect(screen, (100, 100, 100), map.rect, 0)

            pygame.draw.rect(screen, (200, 200, 200), map.rect, 1)

        for button in buttons:
            pygame.draw.rect(screen, (100, 100, 100), button.rect, 1)

        for tool in tools:
            if tool.state == 2:
                sprite = pygame.image.load("Assets/wall.png")
                screen.blit(sprite, (tool.rect))

            pygame.draw.rect(screen, (100, 100, 100), tool.rect, 1)

        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            for map in maps:
                if pygame.mouse.get_pressed()[0]:
                    hover = True
                else:
                    hover = False
                if hover and mouse[0] > map.rect.x and mouse[0] < map.rect.x+25 and mouse[1] > map.rect.y and mouse[1] < map.rect.y+25:
                    if current != 0:
                        map.state = current
                    print("tiler:", map.id, " /// state:",map.state, " /// rest:", map.id % 38, " /// times:",map.id // 38)

            for tool in tools:
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and mouse[0] > tool.rect.x and mouse[0] < tool.rect.x+50 and mouse[1] > tool.rect.y and mouse[1] < tool.rect.y+50:
                    current = tool.state
                    print("clicking in tool:", tool.id, " /// state:",tool.state)
            for button in buttons:
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and mouse[0] > button.rect.x and mouse[0] < button.rect.x + 200 and mouse[1] > button.rect.y and mouse[1] < button.rect.y + 50:
                    Export(maps)
            if event.type == pygame.QUIT:
                exit(0)

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    pygame.init()
    from os import environ
    environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (30, 25)
    pygame.display.set_caption("Game")
    screen = pygame.display.set_mode((1300, 700))

    clock = pygame.time.Clock()
    Main()
