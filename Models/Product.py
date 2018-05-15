from Models.Object import *


class Product(Object):

    """
    -------------
    public:
    -------------

    ------------
    protected:
    ------------
    string      _name

    -------------
    public:
    -------------
    void        _setName(string name)
    string      _getName
    void        _printInfo()

    ------------
    protected:
    ------------

    """

    def __init__(self, name, size=(60, 60), position=(0, 0), normalImage=None):
        super().__init__(name, size, position, normalImage)


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
