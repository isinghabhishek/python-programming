import math

c = 0
num = int(input("Enter a number"))
a = math.ceil(num**0.5)
for i in range(1,a+1):
    if (num%i==0):
        if i==(num*0.5):
            print(i)
            c=c+1
        else:
            print(i)
            print(num/i)
            c=c+2
            print(c)

