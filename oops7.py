import csv

class iteam:

    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            return False
        elif isinstance(num,int):
            return True
        else:
            return False

print(iteam.is_integer(5))