#using for loop to itterate on two diffrent list
list1=[1,2,3,"narwa","liza"]
list2=[4,6,7,'jsr',"musabani"]
for x,y in zip(list1,list2):
    print(x,y)
#for loop accepting 2 arguments can run only with zip objct not with list or others


#real life examples regarding zip
CP=[100,200,300,400,500]
SP=[50,60,200,1000,570]
for x,y in zip(CP,SP):
    print(x-y)