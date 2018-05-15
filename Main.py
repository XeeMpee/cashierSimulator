import pygame
from Models.Object import *
from View.MainWindow import *
from Control.Settings import Settings
from Control.GameController import *


def eventsQueue(obj1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                return False
            if event.key == pygame.K_s:
                tmpScale(obj1, 160, 160)
            if event.key == pygame.K_r:
                tmpScale(obj1, 60, 60)
    return True


def tmpScale(obj, x, y):
    obj.setSize(x, y)
    pass


if __name__ == "__main__":
    print("Hello Darkness, my old friend!")

    # settings = Settings.getInstance()
    #
    # pygame.init()
    # windowSize = (1080, 720)
    # fps = 60
    # pygameClock = pygame.time.Clock()
    # screen = pygame.display.set_mode(settings.windowSize)
    #
    # spriteGroup = pygame.sprite.Group()
    # normalImage = pygame.image.load("./Files/blender.png")
    # sprite1 = Object(normalImage, (60, 60), (40, 40))
    # spriteGroup.add(sprite1)
    # spriteGroup.draw(screen)
    #
    # con = True
    # while con:
    #     screen.fill((255, 255, 255))
    #     con = eventsQueue(sprite1)
    #
    #     spriteGroup.draw(screen)
    #     pygame.display.update()
    #     pygameClock.tick(fps)

    # mainWindow = MainWindow()
    # mainWindow.run()

    game = GameController()
    game.run()
