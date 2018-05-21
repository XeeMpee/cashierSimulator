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
        self._weight = round(weight, 2)
        self._weightValue = None

    def setWeight(self, weight):
        if weight < 0:
            raise MyQuantityException("Product amount must be greater than 0!")
        self._weight = round(weight, 2)
        pass

    def getWeight(self):
        return self._weight

    def getWeightValue(self):
        return self._weightValue


    # Overwrite
    def printInfo(self):
        super().printInfo()
        print("Weight: {}".format(self._weight))

    def setLabel(self, hidden=False):
        if hidden is False:
            self._label = self._name.title() + ":" + str(self._weight) + "kg"
        else:
            self._label = self._name.title() + ":?" + "kg"
            self._weightValue = round(self._weight, 2)

    def getValue(self):
        return self._weight


    def getProductsNumber(self):
        return 1