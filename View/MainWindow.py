import pygame
from Control.Settings import *
from Models.Product import *
import Colors

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


    -------------
    public:
    -------------
    void            gameLoop()
    void            addToProductsSpriteGroup(Sprite productObject)
    void            addToAnotherSpriteGroup(Sprite obj)

    void            fillScreen()

    void            drawProducts()
    void            drawAnotherSprites()

    void            setProductsPositions(Product[] products)

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

    def addToAnotherSpriteGroup(self, obj):
        self.__anotherSpriteGroup.add(obj)

    def fillScreen(self):
        self._screen.fill(self._settings.backgroundColor)

    def drawProducts(self):
        self.__productsSpriteGroup.draw(self._screen)

    def drawAnotherSprites(self):
        self.__anotherSpriteGroup.draw(self._screen)

    def setProductsPositions(self, products):

        for i in range(0, len(products)):
            Product(i).setPosition()

        pass



