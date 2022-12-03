
a=int(input("Enter the hour time:-"))
b=int(input("Enter the minute time-"))
c=input("Enter the AM or PM in Capital:-")
if(c=='AM'):
    print(a,":",b)
else:
    print(a+12,":",b)