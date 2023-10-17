class iteam:
    payrate=0.8 #class level attribute
    def __init__(self,name:str,price:float,quantity:int=0):
        #Assert validation to receive argument
        assert price>=0, f"Price {price} is not greater than or equal to 0"
        assert quantity>=0, f"quantity {quantity} is not greater than or equal to 0"


        #Assign to self object
        self.name=name
        self.price=price
        self.quantity=quantity

    def calculate_price(self):
        return self.price*self.quantity


iteam1=iteam("phone",40000,2)

iteam2=iteam("Laptop",80000,2)


print(iteam1.calculate_price())
print(iteam2.calculate_price())

print(iteam.payrate)
print(iteam.__dict__)   #class level attributes
print(iteam1.__dict__)  #object level attributes
