import pygame

class Creator(object):
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 25, 25)


def Main():
    running = True

    map = []

    x = y = 25

    for row in range(26):
        for col in range(38):
            map += [Creator(x,y)]
            x+=25
        y+=25
        x=25


    while running:
        screen.fill((0, 0, 0))

        for ma in map:
            pygame.draw.rect(screen, (100, 100, 100), ma.rect, 1)



        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(0)

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
