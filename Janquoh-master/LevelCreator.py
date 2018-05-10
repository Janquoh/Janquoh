import pygame

class Creator(object):
    def __init__(self, x, y, id):
        self.id = id
        self.rect = pygame.Rect(x, y, 25, 25)
        self.state = 0

class Tool(object):
    def __init__(self, x, y, id):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.id = id

def Main():
    running = True

    maps = []
    tools = []

    x = 1050
    y = 25
    id = 0

    for row in range(8):
        for col in range(4):
            id+=1
            tools += [Tool(x, y, id)]
            x+=50
        y+=50
        x=1050

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
            pygame.draw.rect(screen, (100, 100, 100), map.rect, 1)

        for tool in tools:
            pygame.draw.rect(screen, (100, 100, 100), tool.rect, 1)

        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            for map in maps:
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and mouse[0] > map.rect.x and mouse[0] < map.rect.x+25 and mouse[1] > map.rect.y and mouse[1] < map.rect.y+25:
                    print("clicking in tile:", map.id)
            for tool in tools:
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and mouse[0] > tool.rect.x and mouse[0] < tool.rect.x+50 and mouse[1] > tool.rect.y and mouse[1] < tool.rect.y+50:
                    print("clicking in tool:", tool.id)

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
