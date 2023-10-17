class iteam:
    def __init__(self,name:str,price:int,quantity=0):
        assert price>0 , "Price less than 0"
        print("I am a constructor having value : "+name)
        self.name=name
        self.price=price
        self.quantity=quantity

    def calculate_price(self):
        return self.price*self.quantity


iteam1=iteam("phone",0,4)

iteam2=iteam("Laptop",80000,2)

print(iteam1.name)
print(iteam2.name)
print(iteam1.price)
print(iteam2.price)
print(iteam1.quantity)
print(iteam2.quantity)

print(iteam1.calculate_price())
print(iteam2.calculate_price())
