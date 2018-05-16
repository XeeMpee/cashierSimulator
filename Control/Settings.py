import Colors


class Settings:
    __instance = None

    @staticmethod
    def getInstance():
        if Settings.__instance is None:
            Settings()
        return Settings.__instance

    def __init__(self):
        if Settings.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Settings.__instance = self

            # Window:
            self.windowSize = 1380, 780
            self.windowTittle = "CashierSimulator"
            self.backgroundColor = Colors.white
            self.windowIcon = None

            # Plate:
            self.plateSize = 600, 600
            self.platePosition = 40, 120

            # NewCustomerButton
            self.newCustomerButtonPosition = 35, 20
            self.newCustomerButtonSize = 350, 100

            # Products:
            self.maxAmount = 50
            self.maxWeight = 2
            self.minWeight = 0.05

            self.normalSize = (100, 100)
            self.scaledSize = (150, 150)

            # position borders:
            # |------------|
            # |0         1 |
            # |            |
            # |2         3 |
            # |------------|
            self.__marginX = 100
            self.__marginY = 100
            self.productsBorders = [(self.platePosition[0]+self.__marginX, self.platePosition[1] + self.__marginY),
                                    (self.platePosition[0] + self.plateSize[0] - self.__marginX, self.platePosition[1] + self.__marginY),
                                    (self.platePosition[0] + self.__marginX, self.platePosition[1] + self.plateSize[1] - self.__marginY),
                                    (self.platePosition[0] + self.plateSize[0] - self.__marginX, self.platePosition[1] + self.plateSize[1] - self.__marginY)]


            # Scale Coeff:
            self.productBasicSize = 100, 100
            self.productScaledSize = 160, 160

