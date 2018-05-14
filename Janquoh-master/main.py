import pygame, game
from levels import Lvl1

def Main():

    player = game.Player()
    walls = game.LoadLevel(Lvl1())

    while True:
        screen.fill((0, 0, 0))

        player.Controls(walls)

        player.Update()
        for bullet in player.bullets:
            bullet.Update()

        for wall in walls:
            if wall.type == 1:
                pygame.draw.rect(screen, (200, 200, 200), wall.rect)
            if wall.type == 2:
                pygame.draw.rect(screen, (100, 100, 100), wall.rect)
                if wall.rect.colliderect(player.hitBox):
                    if wall.side == 1:
                        player.rect.y = 625
                        player.hitBox.y = 625
                    if wall.side == 2:
                        player.rect.x = 50
                        player.hitBox.x = 50
                    if wall.side == 3:
                        player.rect.y = 50
                        player.hitBox.y = 50
                    if wall.side == 4:
                        player.rect.x = 925
                        player.hitBox.x = 925
                    walls = game.LoadLevel(wall.level)

        screen.blit(player.image, player.rect)

        for bullet in player.bullets:
            screen.blit(bullet.image, bullet.rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

        clock.tick(60)
        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    from os import environ
    environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (150, 30)
    pygame.display.set_caption("Game")
    screen = pygame.display.set_mode((1000, 700))

    clock = pygame.time.Clock()
    Main()
