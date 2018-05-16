import pygame
from Models.Object import *


class Button(Object):

    """
    -------------
    public:
    -------------

    ------------
    protected:
    ------------
    Surface         _clickedImage
    bool(flag)      _blocked

    -------------
    public:
    -------------

    ------------
    protected:
    ------------

    """

    def __init__(self, name, size=(60, 60), position=(0, 0), normalImage=None, clickedImage=None):
        super().__init__(name, size, position, normalImage)
        self._clickedImage = clickedImage
        self._blocked = False

    def clicked(self):
        if self._blocked is False:
            self.block()
        elif self._blocked is True:
            # self.unblock()
            return

    def block(self):
        self._blocked = True
        self.image = pygame.transform.scale(self._clickedImage, self._size)

    def unblock(self):
        self._blocked = False
        self.image = pygame.transform.scale(self._normalImage, self._size)

    def getBlockedFlag(self):
        return self._blocked

    def hardSetBlockedFlag(self, boolValue):
        self._blocked = boolValue

