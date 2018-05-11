from pygame import *


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
    u_int(2)    _position
    u_int(2)    _size
    u_int(2)    _scaledSize


    Surface     _normalImage
    Surface     _scaledImage

    -------------
    public:
    -------------
    void        setPosition(u_int x, u_int y)


    ------------
    protected:
    ------------
    void        _spriteInit()
    u_int(2)    _sizeScale(double scaleCoeff)

    """

    # Constructors:
    def __init__(self, normalImage, scaledImage, clickedImage, position=(0, 0), size=(10, 10), scaleCoeff=1.5):

        # Position, size, controlVariables:
        self._position = position

        self._size = size
        self._scaledSize = self._sizeScale(scaleCoeff)

        # LookOut:
        self._normalImage = normalImage
        self._scaledImage = scaledImage
        self._clickedImage = clickedImage
        self.image = None


    # Public:

    def setPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self._position[0] = x
        self._position[1] = y
        pass

    # Protected:

    def _spriteInit(self):

        self._normalImage = pygame.transform.scale(self._normalImage, self._size)
        self._scaledImage = pygame.transform.scale(self._scaledImage, self._scaledSize)

        self.image = self._normalImage
        self.rect = self.image.get_rect()
        pass

    def _sizeScale(self, scaleCoeff):
        a = self._size[0]*scaleCoeff // 1
        b = self._size[1]*scaleCoeff // 1
        return a, b
        pass

