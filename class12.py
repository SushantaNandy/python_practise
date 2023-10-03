#set methods
a={'delhi','mumbai','kolkata','jamshedpur'}
b={'delhi','mumbai','kolkata','jamshedpur','london'}
#adding an iteams
a.add("bbsr")
print(a)
#removing an element
a.remove("kolkata")
print(a)
#dicard ---> removing iteams
a.discard("bbsr")
print(a)
#pop---> removing iteams. what ever value is in the end it will remove it
a.pop()
print(a)
#union
d={'delhi','mumbai','kolkata','jamshedpur'}
e={'delhi','mumbai','kolkata','jamshedpur','london'}
c=d.union(e)
print(c)    #use to join two sets
#symmetric diffrence----> shows what is not duplicates
f=d.symmetric_difference(e)
print(f)
#is_subset()---> check weather one set is subset of others
print(d.issubset(e))
#issuperset()---> check weather one set is super set of other
print(d.issuperset(e))   #because d is sub-set of e and e is super-set of d
print(e.issuperset(d))