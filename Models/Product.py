from Models.Object import *
from Control.Settings import *


class Product(Object):

    """
    -------------
    public:
    -------------

    ------------
    protected:
    ------------
    string      _name
    bool(flag)  _scaled
    Settings   __settings

    -------------
    public:
    -------------
    void        setName(string name)
    string      getName
    void        printInfo()
    void        clicked()
    bool        scaled()
    bool        setScaled(bool value)
    bool        scale()

    ------------
    protected:
    ------------

    """

    def __init__(self, name, size=(60, 60), position=(0, 0), normalImage=None):
        super().__init__(name, size, position, normalImage)
        self._scaled = False
        self.__settings = Settings.getInstance()
        self._label = None


    def setName(self, name):
        self._name = name
        pass


    def getName(self):
        return self._name


    def printInfo(self):
        print(
            "Product:\n"
            "Name: {}\n"
            "Image: {}\n"
            "Size: {}\n"
            "Position: {}\n"
            .format(self._name, self.image, self._size, self._position), end="")

    def printName(self):
        print(self._name)


    def clicked(self):
        pass

    def scale(self):
        if self._scaled is False:
            self._scaled = True
            sizeX = self.__settings.scaledSize[0]
            sizeY = self.__settings.scaledSize[1]
            self.setSize(sizeX, sizeY)
            self.rect = self.image.get_rect()
            posX = (self._position[0] - self._size[0] / 6) // 1
            posY = (self._position[1] - self._size[1] / 6) // 1
            self.setPosition(posX, posY)
            # TODO: Ma odszkalowywać! xD

    def descale(self):
        if self._scaled is True:
            self._scaled = False

            posX = (self._position[0] + self._size[0] / 6) // 1
            posY = (self._position[1] + self._size[1] / 6) // 1
            self.setPosition(posX, posY)

            sizeX = self.__settings.normalSize[0]
            sizeY = self.__settings.normalSize[1]
            self.setSize(sizeX, sizeY)
            # self.rect = self.image.get_rect()


    def setLabel(self, hidden=False):
        pass

    def getLabel(self):
        return self._label
