#manupulation of strings
#strings methods

#length functions
#returns the no. of iteams in an object. If object is string it will return the length of the string

a="moolya acedemy"
print(len(a))

#str()---> convert the specific value to string
b=1234
print(str(b))
c=str(b)  # now for checking weather converted to string or not
print(c[0])

#find()---> search the string for a specific value and return the position
print(c.find("3"))

#upper()---> convert the string to upper case
#lower()---> convert t lower case
print(a.upper())

#count()---> returns the number of times a specific value is found in the string. If u want to be very specific
#then give start and end index


z="i love my country very much. I can die for my country. I love it."
print(z.count("love"))
print(z.count("love", 2,30))

#isupper()---> return true if evry thing is in upper and vice versa in islower()

print(z.isupper())
print(z.islower())

y=z.upper()
print(y.isupper())

#split()--> it split the string at the specific seperator and return a list
#if nothing is spefied as seperator then white space  is considered

print(z.split())
print(z.split("very"))

#rsplit---> split the string from the right
print(z.rsplit())

#strip()--> it returned the trimmed version of the string
g="         54446464i love moolya     "
print(g.strip())  #if no argument is passed then it ommit white space only from both end
print(g.strip('54446464 '))
print(g.lstrip('54446464 '))
print(g.rstrip('54446464 '))

#replace()--> we can replace a specific phrase or a sub-string with another specific pharase
print(a.replace("moolya","infsys"))

#find()---> it searches for the specify value and return the position
print(g.find("moolya"))