#sets
#set is an un-ordered datacollection with no duplicates elements
#use---> membership testing, elements duplicates entry
a={10,20,30,40}
b={10,'20',.30} #combinations of datatypes
print(b)
c={10,20,30,40,'40',40}
print(c)  # no duplicates value is taken
#another way for defining sets
d= set(("48",48,10,20))
print(d)
#finiding length of the set
print(len(c))  #ignored the duplicates values while finding length
#membership operator---> find weather particular element is there in the set or not
print(40 in c)