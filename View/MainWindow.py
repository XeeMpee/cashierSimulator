import pygame
# from tkinter import *
# from tkinter import messagebox
from pygame import freetype
from Control.Settings import *
from Models.Product import *
import Colors
import random
from Models.Button import *
from View.TexturesMenager import *

class MainWindow:

    """
    -------------
    public:
    -------------

    ------------
    protected:
    ------------
    Surface         _screen
    Settings        _settings
    Group           _productsSpriteGroup
    Group           _anotherSpriteGroup
    Group           _buttonsGroup


    -------------
    public:
    -------------
    void            gameLoop()
    void            addToProductsSpriteGroup(Sprite productObject)
    void            clearProductsSpriteGroup()
    void            addToAnotherSpriteGroup(Sprite obj)
    void            addToButtonsGroup(Button obj)

    void            fillScreen()

    void            drawProducts()
    void            drawAnotherSprites()
    void            drawButtonsSprites()

    void            setProductsPosition(Product product)
    void            setProductPosition()

    ------------
    protected:
    ------------
    void            _setScreen(u_int(2) resolution, string tittle, * icon)
    void            _setBackground
    bool            _eventsQueue()
    """

    def __init__(self):
        self._settings = Settings.getInstance()

        # SetScreen:
        self._screen = None
        self._setScreen()

        # Background:
        self._fillColor = self._settings.backgroundColor

        # SpriteGroups:
        self.__productsSpriteGroup = pygame.sprite.Group()
        self.__anotherSpriteGroup = pygame.sprite.Group()
        self.__buttonsGroup = pygame.sprite.Group()

        # Font
        pygame.font.init()
        pygame.freetype.init()
        self.font = pygame.font.SysFont(self._settings.cashRegisterValueFont, self._settings.cashRegisterValueSize)
        self.productFont = pygame.freetype.SysFont("Liberation Serif", 20)
        pass


    def _setScreen(self):
        # Settings form SettingSingleton:
        resolution = self._settings.windowSize
        tittle = self._settings.windowTittle
        icon = self._settings.windowIcon

        # Setting window parameters:
        self._screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption(tittle)
        # TODO: set icon!
        pass

    def addToProductsSpriteGroup(self, productObj):
        self.__productsSpriteGroup.add(productObj)

    def clearProductsSpriteGroup(self):
        self.__productsSpriteGroup.empty()

    def addToAnotherSpriteGroup(self, obj):
        self.__anotherSpriteGroup.add(obj)

    def addToButtonsSpriteGroup(self, obj):
        self.__buttonsGroup.add(obj)

    def fillScreen(self):
        self._screen.fill(self._settings.backgroundColor)

    def drawProducts(self):
        self.__productsSpriteGroup.draw(self._screen)

    def drawAnotherSprites(self):
        self.__anotherSpriteGroup.draw(self._screen)

    def drawButtons(self):
        self.__buttonsGroup.draw(self._screen)
    #
    # def setProductsPosition(self, product):
    #     product.setPosition()
    #     pass

    def setProductsPosition(self, obj):

        x = random.randint(self._settings.productsBorders[0][0], self._settings.productsBorders[1][0])
        y = random.randint(self._settings.productsBorders[0][1], self._settings.productsBorders[2][1])
        obj.setPosition(x, y)
        return obj

    def productScaleAnimation(self, product):
        x, y = pygame.mouse.get_pos()
        try:
            if product.rect.collidepoint(x, y):
                product.scale()
            else:
                product.descale()
        except AttributeError:
            pass
        pass

    def cashRegisterButtonPlace(self, cashierButtons):
        positionX = self._settings.buttonsPositionStart[0]
        positionY = self._settings.buttonsPositionStart[1]
        for i in range(0, 12):
            if i % 3 == 0:
                positionY += self._settings.buttonDistanceY
                positionX = self._settings.buttonsPositionStart[0]
            cashierButtons[i].setPosition(positionX, positionY)
            positionX += self._settings.buttonDistanceX

        positionX = self._settings.longButtonsPositionStart[0]
        positionY = self._settings.longButtonsPositionStart[1]
        for i in range(12, len(cashierButtons)):
            positionY += self._settings.longButtonDistanceY
            cashierButtons[i].setPosition(positionX, positionY)
            positionX += self._settings.longButtonDistanceX


        pass

    def displayCashRegisterValue(self, value):
        value = str(value)
        text = self.font.render(value, True, self._settings.cashRegisterValueColor)
        position = self._settings.cashRegisterValuePosition[0] - 25 * len(value), self._settings.cashRegisterValuePosition[1]

        if len(value) >= 13:
            errorText = "ERROR!"
            text = self.font.render(errorText, True, self._settings.cashRegisterValueColor)
            position = self._settings.cashRegisterValuePosition[0] - 30 * len(errorText), self._settings.cashRegisterValuePosition[1]

        self._screen.blit(text, position)
        pass


    def displayProductLabel(self, obj):
        if obj is None:
            return
        label = obj.getLabel()
        text = self.productFont.render(label, (255, 255, 255), (0, 0, 0), pygame.freetype.STYLE_DEFAULT, 0, 20)
        position = list(obj.getPosition())
        position[0] += self._settings.productLabelDisplace[0]
        position[1] += self._settings.productLabelDisplace[1]
        self._screen.blit(text[0], position)


    def showLoseMessage(self, points):

        class tmpClass:
            def __init__(self, screen, points):
                self.points = points
                self._screen = screen

                self.looseMessageLabel = "GameOver! You Loose :("
                self.looseMessagePosition = 250, 200
                self.pointsMessage = "Your score: " + str(points)
                self.pointsMessagePosition = 600, 300
                self.font = pygame.freetype.SysFont("Liberation Serif", 80, True)
                self.pointsFont = pygame.freetype.SysFont("Liberation Serif", 40, True)

                TextureMenager.buttonsTexturesAppend("quit")
                TextureMenager.buttonsTexturesAppend("quitClicked")
                TextureMenager.buttonsTexturesAppend("tryagain")
                TextureMenager.buttonsTexturesAppend("tryagainClicked")

                self.buttons = []
                self.tryagainButton = Button("tryagain", (300, 150), (300, 400), TextureMenager.getButtonTextures("tryagain"), TextureMenager.getButtonTextures("tryagainClicked"))
                self.quitButton = Button("quit", (300, 150), (800, 400), TextureMenager.getButtonTextures("quit"), TextureMenager.getButtonTextures("quitClicked"))
                self.spritesGroup = pygame.sprite.Group()
                self.spritesGroup.add(self.tryagainButton)
                self.spritesGroup.add(self.quitButton)
                self.buttons.append(self.quitButton)
                self.buttons.append(self.tryagainButton)

                pass

            def showLabel(self):
                text = self.font.render(self.looseMessageLabel, (0, 0, 0))
                points = self.pointsFont.render(self.pointsMessage, (0, 0, 0))
                self._screen.blit(text[0], self.looseMessagePosition)
                # self._screen.blit(points[0], self.pointsMessagePosition)

            def localEventsQueue(self):
                for event in pygame.event.get():
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_ESCAPE:
                            return False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print("clicked")
                        x, y = pygame.mouse.get_pos()
                        for i in self.buttons:
                            if i.rect.collidepoint(x, y):
                                print("BUTTON CLICKED!")
                                i.block()

                    if event.type == pygame.MOUSEBUTTONUP:
                        x, y = pygame.mouse.get_pos()
                        for i in self.buttons:
                            i.unblock()
                            if i.rect.collidepoint(x, y):
                                if i.getName() == "quit":
                                    i.clicked()
                                    exit(0)
                                    return 0
                                if i.getName() == "tryagain":
                                    i.clicked()
                                    return 2

                                pass

                        pass
                return True
                pass


        controlClass = tmpClass(self._screen, points)
        con = 1
        while con == 1:
            self.fillScreen()
            controlClass.showLabel()
            controlClass.spritesGroup.draw(self._screen)
            con = controlClass.localEventsQueue()
            pygame.display.update()

        if con == 2:
            return True

        if con == 0:
            return False


    def showWinMessage(self, myTime, average):

        class tmpClass:

            def __init__(self, screen, myTime, average):
                self._screen = screen
                self._myTime = myTime
                self._average = average

                self.spritesGroup = pygame.sprite.Group()

                self.looseMessageLabel = "Good Job! Your results:"
                self.looseMessagePosition = 250, 200
                self.timeMessage = "Time: " + str(self._myTime)
                self.averageTimeMessage = "Average time: " + str(self._average)
                self.timeMessagePosition = 250, 300
                self.avTimeMessagePosition = 250, 350
                self.font = pygame.freetype.SysFont("Liberation Serif", 80, True)
                self.timeFont = pygame.freetype.SysFont("Liberation Serif", 40, True)

                TextureMenager.buttonsTexturesAppend("quit")
                TextureMenager.buttonsTexturesAppend("quitClicked")
                TextureMenager.buttonsTexturesAppend("tryagain")
                TextureMenager.buttonsTexturesAppend("tryagainClicked")

                self.buttons = []
                self.tryagainButton = Button("tryagain", (300, 150), (300, 500), TextureMenager.getButtonTextures("tryagain"), TextureMenager.getButtonTextures("tryagainClicked"))
                self.quitButton = Button("quit", (300, 150), (800, 500), TextureMenager.getButtonTextures("quit"), TextureMenager.getButtonTextures("quitClicked"))
                self.spritesGroup = pygame.sprite.Group()
                self.spritesGroup.add(self.tryagainButton)
                self.spritesGroup.add(self.quitButton)
                self.buttons.append(self.quitButton)
                self.buttons.append(self.tryagainButton)

                pass

            def showLabel(self):
                text = self.font.render(self.looseMessageLabel, (0, 0, 0))
                timeRes = self.timeFont.render(self.timeMessage, (0, 0, 0))
                avTimeRes = self.timeFont.render(self.averageTimeMessage, (0, 0, 0))
                self._screen.blit(text[0], self.looseMessagePosition)
                self._screen.blit(timeRes[0], self.timeMessagePosition)
                self._screen.blit(avTimeRes[0], self.avTimeMessagePosition)

            def localEventsQueue(self):
                for event in pygame.event.get():
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_ESCAPE:
                            return False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print("clicked")
                        x, y = pygame.mouse.get_pos()
                        for i in self.buttons:
                            if i.rect.collidepoint(x, y):
                                print("BUTTON CLICKED!")
                                i.block()

                    if event.type == pygame.MOUSEBUTTONUP:
                        x, y = pygame.mouse.get_pos()
                        for i in self.buttons:
                            i.unblock()
                            if i.rect.collidepoint(x, y):
                                if i.getName() == "quit":
                                    i.clicked()
                                    exit(0)
                                    return 0
                                if i.getName() == "tryagain":
                                    i.clicked()
                                    return 2

                                pass

                        pass
                return True
                pass


        controlClass = tmpClass(self._screen, myTime, average)
        con = 1
        while con == 1:
            self.fillScreen()
            controlClass.showLabel()
            controlClass.spritesGroup.draw(self._screen)
            con = controlClass.localEventsQueue()
            pygame.display.update()


        if con == 2:
            return True

        if con == 0:
            return False

