import pygame, game, GUI
from levels import Lvl1

def Main():

    player = game.Player()
    walls = game.LoadLevel(Lvl1())
    graphicInterface=GUI.characterPortrait()
    heart1 = GUI.heartContainers(43)
    heart2 = GUI.heartContainers(70)
    heart3 = GUI.heartContainers(97)
    skill1 = GUI.skillMap(screen,60,player.QCoolDown,"assets/GoFast.png")
    skill2 = GUI.skillMap(screen,116,player.ECoolDown,"assets/Scare_Chase.png")
    enemyes = []
    enemyes += [game.Enemy()]

    while True:
        screen.fill((0, 0, 0))

        player.Controls(walls)

        player.Update()
        for bullet in player.bullets:
            for wall in walls:
                if wall.rect.colliderect(bullet.rect):
                    player.bullets.remove(bullet)
                    break
            for enemy in enemyes:
                if bullet.rect.colliderect(enemy.rect):
                    player.bullets.remove(bullet)
                    enemy.life -= bullet.demage
                    if enemy.life <= 0:
                        enemyes.remove(enemy)
                    break
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
                        player.rect.x = 150
                        player.hitBox.x = 150
                    if wall.side == 3:
                        player.rect.y = 50
                        player.hitBox.y = 50
                    if wall.side == 4:
                        player.rect.x = 1025
                        player.hitBox.x = 1025
                    walls = game.LoadLevel(wall.level)

        screen.blit(player.image, player.rect)
        screen.blit(graphicInterface.image, graphicInterface.rect)
        screen.blit(heart1.image, heart1.rect)
        screen.blit(heart2.image, heart2.rect)
        screen.blit(heart3.image, heart3.rect)
        screen.blit(skill1.image, skill1.rect)
        pygame.draw.rect(screen, (2, 25, 255), pygame.Rect(0, 85, 50 / player.QProgress, 5))
        screen.blit(skill2.image, skill2.rect)
        pygame.draw.rect(screen, (255, 25, 2), pygame.Rect(0, 141, 50 / player.EProgress, 5))
        for enemy in enemyes:
            screen.blit(enemy.imageMaster, enemy.rect)

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
    screen = pygame.display.set_mode((1200, 900))

    clock = pygame.time.Clock()
    Main()
