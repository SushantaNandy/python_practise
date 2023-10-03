#zip fuction
#The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is
# #paired together, and then the second item in each passed iterator are paired together etc.

#If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator
list1=["sushanta","madhuri","sharuckh"]
list2=["nandy","dixit","khan"]
s=zip(list1,list2)
print(s)  #it return zip object.
print(list(s))


tup=(1,2,3,4)
tup1=(100,200,300,400,500)
tup3=zip(tup,tup1)
print(tuple(tup3))



