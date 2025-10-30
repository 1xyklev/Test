class Inventory:
    def __init__(self):
        self.__stock = 0

        print(f"새 상품이 등록되었습니다.")

    def get_stock(self):
        return self.__stock
    
    def set_stock(self,amount):
        if amount >= 0:
            self.__stock += amount
        else:
            print("0 이상의 값만 출고됩니다.")

    def add_stock(self, amount):
        if amount >= 0:
            self.__stock += amount
        print(f"{amount}개가 입고되었습니다.")

    def remove_stock(self,amount):
        if 0 < amount <= self.__stock:
            self.__stock -= amount
            print(f"{amount}개가 출고되었습니다.")
        else:
            print(f"현재 재고보다 많은 수량은 출고할 수 없습니다.")
        return self.__stock

item1 = Inventory()
item1.add_stock(10)
item1.remove_stock(3)
print("현재 재고 수랑:", item1.get_stock())

item1.set_stock(20)
print("수정된 재고 수량:", item1.get_stock())