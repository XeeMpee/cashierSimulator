from Models.Product import *
from Control.MyException import *

class RetailProduct(Product):

    """
    -------------
    public:
    -------------

    ------------
    protected:
    ------------
    string      _amount

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

    def __init__(self, name, amount, size=(60, 60), position=(0, 0), normalImage=None ):
        super().__init__(name, size, position, normalImage)
        self._amount = amount

    def setAmount(self, amount):
        if amount < 0:
            raise MyQuantityException("Product amount must be greater than 0!")
        self._amount = amount
        pass

    def getAmount(self):
        return self._amount


    # Overwrite
    def printInfo(self):
        super().printInfo()
        print("Amount: {}".format(self._amount))

    def setLabel(self, hidden=False):
            self._label = self._name.title() + ":" + str(self._amount) + "szt."


    def getValue(self):
        return self._amount
