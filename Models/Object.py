import pygame


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


    Surface     _normalImage

    -------------
    public:
    -------------
    void        setPosition(u_int x, u_int y)
    void        setSize(u_int x, u_int y)


    ------------
    protected:
    ------------
    void        _spriteInit()
    u_int(2)    _sizeScale(double scaleCoeff)

    """

    # Constructors:
    def __init__(self, normalImage, scaledImage, clickedImage, position=(0, 0), size=(10, 10), scaleCoeff=1.5):

        # Sprite constructor:
        super().__init__()

        # Position, size, controlVariables:
        self._position = list(position)
        self._size = list(size)
        self.rect = None

        # LookOut:
        self._normalImage = normalImage
        self.image = None

        # SpriteInit:
        self._spriteInit()

    # Public:

    def setPosition(self, x, y):
        # TODO: Exception: x<0; y<0
        self.rect.x = x
        self.rect.y = y
        self._position[0] = x
        self._position[1] = y
        pass

    def setSize(self, x, y):
        # TODO: Exception: x<0; y<0
        self.image = self._normalImage
        pass

    # Protected:

    def _spriteInit(self):

        self._normalImage = pygame.transform.scale(self._normalImage, self._size)

        self.image = self._normalImage
        self.rect = self.image.get_rect()
        self.setPosition(self._position[0], self._position[1])
        pass


