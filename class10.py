#list methods
#list.append(s) ---> add on iteams to the end of the list
#list.insert(i,x)----> insert an iteam at a given position
#list.remove(x)----> remove the first iteam from the list whose value is equal to x
#list.pop([i])---> Removing iteam from the particular position
#list.index(x)---->
#list.count(x)-----> return the number of times x appears in the list
#list.sort----> sot the iteams in the list in place
#list.copy()---> return the shallow copy of the list
#list.clear()----> will clear the list
cities=["delhi","mumbay","kolkata"]
print(cities)
cities.append("jamshedpur")
print(cities)  #1
#2
cities.insert(1,"narwa")
print(cities)
#3
cities.remove("narwa")
print(cities)
#if two values are there then the first one will be removed
cities.insert(1,"jamshedpur")
print(cities)
cities.remove("jamshedpur")
print(cities)
#4
print(cities.index("jamshedpur"))
#5
print(cities.count("jamshedpur"))
#6
cities.sort()
print(cities)  # sort in alphabetic order
#7
cities.reverse()
print(cities)
#8
new_cities= cities.copy()
print(new_cities)
#9
print(new_cities.clear())