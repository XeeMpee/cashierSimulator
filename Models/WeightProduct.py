from Models.Product import *
from Control.MyException import *


class WeightProduct(Product):

    """
    -------------
    public:
    -------------

    ------------
    protected:
    ------------
    string      _weight

    -------------
    public:
    -------------
    void        _setAmount(string name)
    string      _getAmount
    void        _printInfo()

    ------------
    protected:
    ------------

    """

    def __init__(self, name, weight, size=(60, 60), position=(0, 0), normalImage=None ):
        super().__init__(name, size, position, normalImage)
        self._weight = weight

    def setWeight(self, weight):
        if weight <= 0:
            raise MyQuantityException("Product amount must be greater than 0!")
        self._weight = weight
        pass

    def getWeight(self):
        return self._weight


    # Overwrite
    def printInfo(self):
        super().printInfo()
        print("Weight: {}".format(self._weight))
