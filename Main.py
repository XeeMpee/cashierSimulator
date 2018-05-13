import pygame
from Models.Object import *


def eventsQueue():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                return False
    return True


if __name__ == "__main__":
    print("Hello Darkness, my old friend!")

    pygame.init()
    windowSize = (1080, 720)
    fps = 60
    pygameClock = pygame.time.Clock()
    screen = pygame.display.set_mode(windowSize)

    spriteGroup = pygame.sprite.Group()
    normalImage = pygame.image.load("./Files/blender.png")
    sprite1 = Object(normalImage, normalImage, normalImage, (40, 40), (60, 60))
    spriteGroup.add(sprite1)
    spriteGroup.draw(screen)

    con = True
    while con:
        screen.fill((255, 255, 255))
        con = eventsQueue()

        spriteGroup.draw(screen)
        pygame.display.update()
        pygameClock.tick(fps)


