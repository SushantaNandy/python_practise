class Iteams:
    pass
Iteam1=Iteams()
#Assigning attributes to instances
Iteam1.name="phone"
Iteam1.price=40000
Iteam1.quantity=5
print(type(Iteam1.price))

class iteam:
    def __init__(self):
        print("I am a constructor")
    def calculate_price(self,price,quantity):
        return price*quantity


iteam1=iteam()

class li:
    def __init__(self):
        print("heyeghe")

    def check(self):
        return 2

ob1=li()
iteam1.name="phone"
iteam1.price=40000
iteam1.quantity=5

iteam2=iteam()
iteam2.name="Laptop"
iteam2.price=80000
iteam2.quantity=2

print(iteam2.calculate_price(iteam1.price,iteam1.quantity))

