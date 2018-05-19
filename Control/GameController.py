import pygame
from Models.Product import *
from Models.WeightProduct import *
from Models.RetailProduct import *
from Models.Button import *
from Control.Settings import *
from View.TexturesMenager import *
from View.MainWindow import *
import random


class GameController:

    """
    -------------
    public:
    -------------

    ------------
    protected:
    ------------
    Settings            _settings
    Product[]           _allRetailProductsList
    Product[]           _allWeightProductsList
    Product[]           _products
    Product             _actualProduct
    Object              _plate
    Object              _cashRegister
    u_int               _productCounter
    Button[]            _cashierButton

    -------------
    public:
    -------------
    void                run()

    ------------
    protected:
    ------------
    void                _createAllProductsLists()
    void                _generateProducts()
    void                _generateActualProduct()
    bool                _eventsQueue()
    void                _plateCreate()

    """

    def __init__(self):
        self._settings = Settings.getInstance()

        self._allRetailProductsList = []
        self._allWeightProductsList = []
        self._createAllProductsLists()
        self._products = []

        # GameWindow
        self.gameWindow = MainWindow()

        # NewCustomerButton:
        TextureMenager.buttonsTexturesAppend("newCustomer")
        TextureMenager.buttonsTexturesAppend("newCustomerClicked")
        self._newCustomerButton = Button("newCustomerButton", self._settings.newCustomerButtonSize, self._settings.newCustomerButtonPosition, TextureMenager.getButtonTextures("newCustomer"), TextureMenager.getButtonTextures("newCustomerClicked"))
        self.gameWindow.addToButtonsSpriteGroup(self._newCustomerButton)

        # CashRegister:
        TextureMenager.anotherTexturesAppend("cashRegister")
        self._cashRegister = Object("cashRegister", self._settings.cashRegisterSize, self._settings.cashRegisterPosition, TextureMenager.getAnotherTextures("cashRegister"))
        self.gameWindow.addToAnotherSpriteGroup(self._cashRegister)

        # CashRegisterButtons:
        self._cashRegisterButtons = []

        j = 0
        for i in 7, 8, 9, 4, 5, 6, 1, 2, 3, 'dot', 0, 'b':
            TextureMenager.buttonsTexturesAppend(str(i))
            TextureMenager.buttonsTexturesAppend(str(i) + "Clicked")
            self._cashRegisterButtons.append(Button(str(i), self._settings.numberButtonSize, (0,0), TextureMenager.getButtonTextures(str(i)), TextureMenager.getButtonTextures(str(i) + "Clicked")))
            self.gameWindow.addToButtonsSpriteGroup(self._cashRegisterButtons[j])
            j += 1
            pass

        for i in 'clear', 'add', 'weigh', 'done':
            TextureMenager.buttonsTexturesAppend(str(i))
            TextureMenager.buttonsTexturesAppend(str(i) + "Clicked")
            self._cashRegisterButtons.append(Button(str(i), self._settings.longButtonSize, (0,0), TextureMenager.getButtonTextures(str(i)), TextureMenager.getButtonTextures(str(i) + "Clicked")))
            self.gameWindow.addToButtonsSpriteGroup(self._cashRegisterButtons[j])
            j += 1


        self.gameWindow.cashRegisterButtonPlace(self._cashRegisterButtons)

        self._cashRegisterValue = '0'
        # self.gameWindow.displayCashRegisterValue(self._cashRegisterValue)

        # Game Objects:
        TextureMenager.anotherTexturesAppend("plate")
        self._plate = Object("plate", self._settings.plateSize, self._settings.platePosition, TextureMenager.getAnotherTextures("plate"))
        self.gameWindow.addToAnotherSpriteGroup(self._plate)




        self._actualProduct = None
        self._productsCounter = 0


    # Auxiliary funcs:

    def appendToValue(self, n):
        tmpStr = str(self._cashRegisterValue)
        tmpStr += str(n)
        self._cashRegisterValue = str(tmpStr)





    # --------------------------------------------------
    # PreActions:
    def _createAllProductsLists(self):

        for productList, path in [(self._allRetailProductsList, "./Files/Settings/retailProductList.txt"), (self._allWeightProductsList, "./Files/Settings/weightProductList.txt")]:
            f = open(path, "r")
            productName = f.readline()[0:-1]
            while productName != '':
                productList.append(productName)
                TextureMenager.productsTexturesAppend(productName)
                productName = f.readline()[0:-1]

            print("productList: {}" .format(productList))
            print("path: {}" .format(path))
        print("Products names have been loaded!")


    def _generateProducts(self):

        # Value of maximum products quantity:
        numOfProducts = random.randint(1, 20)
        print(numOfProducts)
        # Values of each type quantity. In ratio 50:50:
        numOfWeighProducts = numOfProducts // 2
        numOfRetailProducts = numOfProducts - numOfWeighProducts

        # Clear list every new game:
        self._products.clear()

        # Temporary lists:
        drawnWeightList = []
        drawnRetailList = []

        # Drawing products:
        for i in range(0, numOfWeighProducts):
            con = True
            while con is True:
                drawnProductName = self._allWeightProductsList[random.randint(0, len(self._allWeightProductsList)-1)]
                if drawnProductName not in drawnWeightList:
                    drawnWeightList.append(drawnProductName)
                    tmpA = self._settings.maxWeight - self._settings.minWeight
                    tmpB = self._settings.minWeight
                    weight = random.random()*tmpA+tmpB

                    tmpTexture = TextureMenager.getProductTexture(drawnProductName)
                    size = self._settings.normalSize
                    tmpProduct = WeightProduct(drawnProductName, weight, size, (0, 0), tmpTexture)

                    self._products.append(tmpProduct)
                    # self.gameWindow.addToProductsSpriteGroup(tmpProduct)
                    con = False

        for i in range(0, numOfRetailProducts):
            con = True
            while con is True:
                drawnProductName = self._allRetailProductsList[random.randint(0, len(self._allRetailProductsList)-1)]
                if drawnProductName not in drawnRetailList:
                    drawnRetailList.append(drawnProductName)
                    amountOneOrMany = random.randint(0, 1)
                    if amountOneOrMany == 0:
                        amount = 1
                    else:
                        amount = random.randint(2, self._settings.maxAmount)

                    tmpTexture = TextureMenager.getProductTexture(drawnProductName)
                    size = self._settings.normalSize
                    tmpProduct = RetailProduct(drawnProductName, amount, size, (0, 0), tmpTexture)

                    self._products.append(tmpProduct)
                    # self.gameWindow.addToProductsSpriteGroup(tmpProduct)
                    con = False

        # Randomizing created list:
        random.shuffle(self._products)

        # Display list in terminal:
        for j in self._products:
            j.printInfo()
            print()

        # Display list in terminal:
        for j in self._products:
            j.printName()

        # ActualProductsPreSet:
        self._productsCounter = 0

    # --------------------------------------------------


    # --------------------------------------------------
    # ActualProduct actions:
    def _generateActualProduct(self):
        if self._productsCounter == len(self._products):
            self._actualProduct = None
            self.gameWindow.clearProductsSpriteGroup()
            self._newCustomerButton.unblock()
            return
        self._actualProduct = self._products[self._productsCounter]
        self._productsCounter += 1
        self.gameWindow.clearProductsSpriteGroup()
        self.gameWindow.addToProductsSpriteGroup(self._actualProduct)
        self._actualProduct = self.gameWindow.setProductsPosition(self._actualProduct)
        self._actualProduct.setLabel(True)

    # --------------------------------------------------


    # --------------------------------------------------
    # GameEvents:
    def _eventsQueue(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("QuitButton pressed")
                return False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    print("ESCAPE pressed")
                    return False
                if event.key == pygame.K_g:
                    print("G pressed")
                    self._cashRegisterValue *= 10
                    print(self._cashRegisterValue)
                if event.key == pygame.K_1:
                    print("1 pressed")
                    # self.generateActualProduct()


            if event.type == pygame.MOUSEBUTTONDOWN:
                # cashRegisterButtonsEvents:
                x, y = pygame.mouse.get_pos()
                for i in self._cashRegisterButtons:
                    if i.rect.collidepoint(x, y):
                        if i.getBlockedFlag() is False:
                            i.clicked()

                            buttonName = i.getName()
                            if buttonName == '0':
                                print("0 clicked")
                                if self._cashRegisterValue == '0':
                                    break
                                else:
                                    self.appendToValue(0)
                                    print("appending")
                                pass

                            for j in '1', '2', '3', '4', '5', '6', '7', '8', '9':
                                if buttonName == j:
                                    if self._cashRegisterValue == '0':
                                        self._cashRegisterValue = ''
                                    print(j + "clicked")
                                    self.appendToValue(int(j))
                                pass

                            if buttonName == 'dot':
                                self.appendToValue('.')
                                print("dot clicked")
                                pass
                            elif buttonName == 'b':
                                print("b clicked")
                                pass
                            elif buttonName == 'clear':
                                self._cashRegisterValue = '0'
                                print("clear clicked")
                                pass
                            elif buttonName == 'add':
                                print("add clicked")
                                self._generateActualProduct()
                                pass
                            elif buttonName == 'weigh':
                                print("weigh clicked")
                                pass
                            elif buttonName == 'done':
                                print("done clicked")
                                pass

            if event.type == pygame.MOUSEBUTTONUP:
                # self.newCustomerButtonClick()
                print("clicked")
                x, y = pygame.mouse.get_pos()

                # NewCustomerButtonEvents:
                if self._newCustomerButton.rect.collidepoint(x, y):
                    if self._newCustomerButton.getBlockedFlag() is False:
                        self._generateProducts()
                        self._generateActualProduct()
                    self._newCustomerButton.clicked()

                for i in self._cashRegisterButtons:
                    if i.getBlockedFlag() is True:
                        i.unblock()

                # ProductClicked:
                try:
                    if self._actualProduct.rect.collidepoint(x, y):
                        # self._generateActualProduct()
                        print("ProductClicked")
                except AttributeError:
                    pass
        pass



        return True
    # --------------------------------------------------


    # --------------------------------------------------
    # GameLoop:
    def run(self):
        con = True
        while con:
            self.gameWindow.fillScreen()
            self.gameWindow.drawAnotherSprites()
            self.gameWindow.drawProducts()
            self.gameWindow.displayProductLabel(self._actualProduct)
            self.gameWindow.drawButtons()
            self.gameWindow.displayCashRegisterValue(self._cashRegisterValue)
            self.gameWindow.productScaleAnimation(self._actualProduct)
            con = self._eventsQueue()

            pygame.display.update()
        pass




