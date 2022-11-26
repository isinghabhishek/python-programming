## print()
## for a in S:
##     print({a})
##
a=int(input("Enter the hour time:-"))
b=int(input("Enter the minute time:-"))
c=int(input("Enter the second time:-"))
if(c=='AM'):
    print(a,":",b)
else:
    print(a+12,":",b)
    
