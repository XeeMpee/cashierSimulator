import pygame
from Control.Settings import *
from Models.Product import *
import Colors
import random

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



