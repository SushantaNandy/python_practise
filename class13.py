#tuples

#Tuples are indexed, allow duplicates values and cannot be modified (immutable)
a=(10,20,30)  #stores integers
b=('kolkata','banglore','howrah')
c=(True, False)
d=(True,10,'kolkata',True,'Kolkata')
print(d[0])
#print(d.remove('mumbai')) #so it can't be modified

#finding the length
print(len(d))
#membership operator
print('kolkata' in d)