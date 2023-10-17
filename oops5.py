class iteam:
    payrate=0.8 #class level attribute
    all= []

    def __init__(self,name:str,price:float,quantity:int=0):
        #Assert validation to receive argument
        assert price>=0, f"Price {price} is not greater than or equal to 0"
        assert quantity>=0, f"quantity {quantity} is not greater than or equal to 0"


        #Assign to self object
        self.name=name
        self.price=price
        self.quantity=quantity

        #Actions to executes
        iteam.all.append(self)

    def calculate_price(self):
        return self.price*self.quantity

    def __repr__(self):
        return f"{self.name,self.price,self.quantity}"


iteam1=iteam("phone",40000,2)
iteam2=iteam("Laptop",80000,2)
iteam3=iteam("Cable",5,5)
iteam4=iteam("Mouse",50,5)
iteam5=iteam("Keyboard",200,4)

print(iteam.all)
#printing the name of all the instances
for instance in iteam.all:
    print(instance.name)