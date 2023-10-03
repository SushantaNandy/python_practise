#formating he string

a='I love'
b='my company'
print('welcome '+a+' '+b)

print('welcome %s %s' %(a,b))
print('welcome %s %s' %('sushant',b))

print('welcome {} {}'.format(a,b))  #we can use the formatting

print('welcome {1} {0}'.format(a,b))    #we can use the indeing

print('welcome {about} {company}'.format(about=a,company=b))    #specing with keywords
print('welcome {about} {company}'.format(about="to my cmpany",company="I love my company"))