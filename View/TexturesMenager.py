import pygame


class TextureMenager:

    productsTextures = dict()
    anotherTextures = dict()

    def __init__(self):
        pass

    @staticmethod
    def productsTexturesAppend(key):
        value = pygame.image.load("./Files/ProductsTextures/" + key + ".png")
        TextureMenager.productsTextures[key] = value
        pass

    @staticmethod
    def getProductTexture(key):
        return TextureMenager.productsTextures[key]

    @staticmethod
    def anotherTexturesAppend(key):
        value = pygame.image.load("./Files/AnotherTextures/" + key + ".png")
        TextureMenager.productsTextures[key] = value
        pass

    @staticmethod
    def getAnotherTextures(key):
        return TextureMenager.productsTextures[key]
