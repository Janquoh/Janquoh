import pygame, game, levels

def Main():
    running = True

    player = game.Player(500,350)
    #walls = game.LoadLevel(levels.Lvl1())
    walls = game.LoadLevel(levels.Lvl1())

    while running:
        screen.fill((0,0,0))

        player.Controls(walls)

        pygame.draw.rect(screen, (250, 0, 0), player.rect, 0)



        for wall in walls:
            if wall.type == 1:
                pygame.draw.rect(screen, (200, 200, 200), wall.rect)
            if wall.type == 2:
                pygame.draw.rect(screen, (100, 100, 100), wall.rect)
                if wall.rect.colliderect(player.rect):
                    if wall.side == 1:
                        player.rect.y = 625
                    if wall.side == 2:
                        player.rect.x = 50
                    if wall.side == 3:
                        player.rect.y = 50
                    if wall.side == 4:
                        player.rect.x = 925
                    walls = game.LoadLevel(wall.level)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    pygame.init()
    from os import environ
    environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (150, 30)
    pygame.display.set_caption("Game")
    screen = pygame.display.set_mode((1000, 700))

    clock = pygame.time.Clock()
    Main()