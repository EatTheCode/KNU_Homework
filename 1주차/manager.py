from beverage import Beverage 

class Manager:

    def __init__(self, name):
        self.name = name
        self.account = 0
        self.list = list()
        print("{} 카페 생성 완료")

    def addBeverage(self):
        name = input("음료 이름을 입력하세요 : ")
        for beverage in self.list:
            if beverage.getName() == name:
                print("이미 존재하는 음료입니다.")
                return
        
        price = int(input("음료 가격을 입력하세요 : "))
        self.list.append(Beverage(name, price))
        print("카페 메뉴 추가완료")

    def printBeverages(self):
        print("\n===========음료정보===========")
        for beverage in self.list:
            beverage.print()
        print("\n==============================")

    def sell(self):
        name = input("음료 이름을 입력하세요 : ")
        for beverage in self.list:
            if beverage.getName() == name:
                self.account += beverage.getPrice()
                print("{} 판매 완료".format(beverage.toString()))
                return
        print("존재하지 않는 음료입니다..")

    def print(self):
        print("이름 : {}, 계좌 : {}원".format(self.name, self.account))
