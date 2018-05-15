class MyException(Exception):
    def __init__(self, message):
        self.message = message


class MyTypeException(Exception):
    def __init__(self, message):
        self.message = message


class MyDataRangeException(Exception):
    def __init__(self, message):
        self.message = message


class MyQuantityException(Exception):
    def __init__(self, message):
        self.message = message
