

#write a program to find the factorial of 20
num = int(input("Enter a number to find its factorial: "))

factorial = 1

if num < 0:
    print("No factorial for negative numbers")
elif num == 0:
    print("Factorial for 0: 1")
else:
    for i in range (1, num + 1):
        factorial = factorial * i
        print("Factorial of ", num , ":" , factorial)