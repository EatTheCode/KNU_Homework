class Beverage:

    def __init__(self, name, price):
        self.name = name
        self.price = price
        print("{}원 {}가 추가되었습니다.\n".format(price, name))

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def setName(self, name):
        self.name = name

    def setPrice(self, price):
        self.price = price

    def toString(self):
        return "{}, {}원".format(self.name, self.price)

    def print(self):
        print("{}".format(self.toString()))
