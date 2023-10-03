#methods in tuples

#count---->How many times the value had appeared
d=(True,10,'kolkata',True,'Kolkata')
print(d.count('kolkata'))
#index---> index of cenrtain value
print(d.index(True))
#accessing the values of tuples
print(d[1])
#by using loop
for x in d:
    print(x)
#concat operator
a=(10,20,30)
demo=a+d
print(demo)
#type method----> to check weather it's tuple or not
print(type(demo))
#range of the tuple
print(demo[0:5])
print(demo[-1])  #printing the last element