#   Write A program to print the ways in which a numbers can be represented in the product of the two no's
# sample input: 48             36
# Sample output: 1*48          1*36
#                2*24          2*18
#                3*16          3*12
#                4*12          4*9
#                6*8           6*6

import math
n=int(input("Enter the Input"))
count=0
a=math.ceil(n**0.5)
for i in range(1,a+1):
    if(n%i==0):
        print(i,"*",int(n/i))





