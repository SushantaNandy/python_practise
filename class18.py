#while loop
# i=1
# while i<10:
#     print(i)
#     i=i+1
# print("exit loop")
# #itteration over string
# name="sushant"
# x=0
# while x<len(name):
#     print(name[x])
#     x+=1

a = 0
b = 500
a += 1
for i in range(a,b):
        y = True
        if(str(i) == str(i)[::-1]):
            if(i>2):
                for a in range(2,i):
                    if(i%a==0):
                        y = False
                        break
                if y:
                    print(i)
# num=int(input("Enter a number:"))
# temp=num
# rev=0
# while(num>0):
#     dig=num%10
#     rev=rev*10+dig
#     num=num//10
# if(temp==rev):
#     print("The number is palindrome!")
# else:
#     print("Not a palindrome!")

# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern
def pypart(n):
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing stars
            print("* ", end="")

        # ending line after each row
        print("\r")


# Driver Code
n = 5
pypart(n)
