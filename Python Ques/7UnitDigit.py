
b=int(input("Enter The Base: "))
p=int(input("Enter The Power: "))

b=b%10
p=p%4

result=b**p
print("Unit Digit Obtained:", result%10)