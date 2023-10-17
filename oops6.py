import csv

class iteam:

    @classmethod
    def instace_from_csv(cls):
        with open('iteams.csv','r') as f:
            reader=csv.DictReader(f)    #change to dictonary
            iteams=list(reader)      #change to list

        for i in iteams:
            print(i)

iteam.instace_from_csv()