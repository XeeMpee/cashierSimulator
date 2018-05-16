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
            posX = self.__settings.scaledSize[0]
            posY = self.__settings.scaledSize[1]
            self.setSize(posX, posY)
            # TODO: Ma odszkalowywać! xD
