#string slicing
a='I love my company'
print(a[0])
print(a[-1])  #print the last index
print(a[0:5])  #start at 0 but end in 4
print(a[4:8])  #start from 4 and ends at 7
print(a[0:])  #to print the whole string
print(a[0:-1])  #ommiting the last character of the string

print(a[-7:])  #print the last word
print(a[-7:-2])   #print leaving 2 character

#reversing the string
print(a[::-1])