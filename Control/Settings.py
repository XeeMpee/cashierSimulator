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
            self.windowSize = 1080, 720
            self.windowTittle = "CashierSimulator"
            self.backgroundColor = Colors.white
            self.windowIcon = None

            # Scale Coeff:
            self.productBasicSize = 100, 100
            self.productScaledSize = 160, 160


