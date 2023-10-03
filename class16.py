#methods in dictonary
a={1:'url',2:'url2',3:'url3'}
#get()---> return the value for specific key in the dictonary
print(a.get(1))
#keys()---> return the copy of dictonary's keys. See how many keys are there
print(a.keys())
#iteams()---> return the vlaues of key values pairs in the forms of tuples
print(a.items())
#values()---> return the values only not the keys
print(a.values())
#pop()---> print the iteam with specific keys
print(a.pop(1))
#popiteam()---> remove the last value and the key
print(a.popitem())      #hence dictonaries are in ordered ways
#update()---> adds the specific key-value pairs in the dictonary
a.update({4:'url4'})
print(a)
#clear()--> remove all elements from the dictonary
a.clear()
print(a)