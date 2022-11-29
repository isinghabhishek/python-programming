
# Program for n-th Fibonacci number
#  Fibonnaci Series
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

def fibonnacci(n):
    a=0
    b=1
    if n<0:
        print("Incorrect Input")
    elif n == 0:
        return a
    elif n ==1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return b

n = int(input("Enter the digit: "))
print(fibonnacci(n))
