#   Write A program to find out unit digit of a number raised to a certain power

#   sample input  I1  2343
#                 I2  2347
#    Output:   7     8

import math
n1= int(input("Enter The Digit"))
n2= int(input("Enter The Power"))
j=n1%10
t=n2%4
ans=j**t%10
print(ans)
# if j==0 or 1 or 5 or 6
#         print(j)
# else
#     r=(j**t)%10
#     print(r)

