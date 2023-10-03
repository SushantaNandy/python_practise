#Disconary
#It is collection in which u store as key and value pair. They are changebale and doesnot allows duplicates values.
a={} #empty disconary
print(type(a))
b={1:20,2:10,3:20}
c={1:'url',2:'url2',3:'url3'}
d={'url':1,'url2':2,'url3':3}
#accessing values
print(c[1])   #we get values using the keys values accociated with the dictonary
print(d['url'])
#add iteams in dictonary
c[4]='url4'  # [key]=value
c['url5']=5
print(c)