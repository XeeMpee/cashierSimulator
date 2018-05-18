import pygame
from Control.MyException import *

class Object(pygame.sprite.Sprite):

    """
    -------------
    public:
    -------------
    Surface     image
    Surface     rect

    ------------
    protected:
    ------------
    string      _name
    u_int(2)    _position
    u_int(2)    _basicSize
    u_int(2)    _size

    Surface     _normalImage

    -------------
    public:
    -------------
    void        setPosition(u_int x, u_int y)
    void        setSize(u_int x, u_int y)
    void        setImage(Surface image)

    u_int(2)    getPosition()
    u_int(2)    getSize()

    ------------
    protected:
    ------------
    void        _spriteInit()
    u_int(2)    _sizeScale(double scaleCoeff)

    """

    # Constructors:
    def __init__(self, name, size=(60, 60), position=(0, 0), normalImage=None):

        # Sprite constructor:
        super().__init__()

        # Position, size, controlVariables:
        self._name = name
        self._position = list(position)
        self._basicSize = list(size)
        self._size = list(size)
        self.rect = None

        # LookOut:
        self._normalImage = normalImage
        self.image = None

        # SpriteInit:
        self._spriteInit()

    # Public:

    def setPosition(self, x, y):
        if x < 0 or y < 0:
            raise MyException("x an y must be greater than 0!")

        self.rect.x = x
        self.rect.y = y
        self._position[0] = x
        self._position[1] = y
        pass

    def getPosition(self):
        return self._position[0], self._position[1]

    def getName(self):
        return str(self._name)


    def setSize(self, x, y):
        if x < 0 or y < 0:
            raise MyException("x an y must be greater than 0!")

        self.image = self._normalImage
        self._size = (x, y)
        self.image = pygame.transform.scale(self._normalImage, self._size)
        # self.rect = self.image.get_rect()
        pass

    def getSize(self):
        return self._size[0], self._size[1]


    def setImage(self, image):
        self._normalImage = image
        self.image = image
        pass


    # Protected:

    def _spriteInit(self):

        self.image = self._normalImage
        self.image = pygame.transform.scale(self._normalImage, self._size)
        self.rect = self.image.get_rect()
        self.setPosition(self._position[0], self._position[1])
        pass


