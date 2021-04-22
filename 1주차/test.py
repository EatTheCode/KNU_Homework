from beverage import Beverage 
from manager import Manager

m = Manager(input("이름을 입력하세요 : "))

while True:
    print("1.음료추가")
    print("2.음료판매")
    print("3.음료메뉴")
    print("4.현재정보")
    print("5.종료")
    ans = int(input("번호를 입력하세요 : "))
    if ans == 1:
        m.addBeverage()
    elif ans == 2:
        m.sell()
    elif ans == 3:
        m.printBeverages()
    elif ans == 4:
        m.print()
    elif ans == 5:
        break
    else:
        print("다시 입력해주세요..")
