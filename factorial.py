def factorial(n):
    if n >= 0:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result
    else:
        print("Input a non-negative number")

num = int(input("Enter a number to find its factorial: "))
print(factorial(num))
