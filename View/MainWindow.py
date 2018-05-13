import pygame
from Control.Settings import *
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

    ------------
    private:
    ------------
    Settings        __settings
    Group           __

    -------------
    public:
    -------------
    void            run()

    ------------
    protected:
    ------------
    void            _setScreen(u_int(2) resolution, string tittle, * icon)
    void            _setBackground
    bool            _eventsQueue()
    """

    def __init__(self):
        self.__settings = Settings.getInstance()

        # SetScreen:
        self._screen = None
        self._setScreen()

        # Background:
        self._fillColor = self.__settings.backgroundColor
        pass


    def _setScreen(self):
        # Settings form SettingSingleton:
        resolution = self.__settings.windowSize
        tittle = self.__settings.windowTittle
        icon = self.__settings.windowIcon

        # Setting window parameters:
        self._screen = pygame.display.set_mode(resolution)
        pygame.display.set_caption(tittle)
        # TODO: set icon!
        pass


    def _eventsQueue(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    return False
        return True
        pass


    def run(self):
        con = True
        while con:
            self._screen.fill(self.__settings.backgroundColor)
            con = self._eventsQueue()

            pygame.display.update()
        pass
