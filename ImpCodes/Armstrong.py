# A positive integer is called an Armstrong number if 
# an Armstrong number of 3 digits, 
# the sum of cubes of each digit 
# is equal to the number itself.

n = int(input("Enter The Digit:"))
s = n
b = len(str(n))

sum1 = 0
while n!= 0:
    r = n%10
    sum1 = sum1+(r**b)
    n = n//10

if(s==sum1):
    print("The given Number", s, "is ArmStrong Number")

else:
    print("The given Number", s, "is Not ArmStrong Number")
