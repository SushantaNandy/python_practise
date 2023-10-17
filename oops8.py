class Iteam:
    def __met1(self):
        print("first class method")

    def __init__(self):
        print("I am const of parent class")



class Child(Iteam):
    def __init__(self):
        super().__init__()
        print("I am const of childn class")

    pass


obj = Child()
# obj.met1()

obj.__met1()
