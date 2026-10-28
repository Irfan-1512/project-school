def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("enter the number at least 2 digits: "))

if num < 10:
    print("Please enter a number with at least 2 digits.")
else:
    print(f"The factorial of {num} is {fact(num)}")


    def add(a,b):
        return a+b

    print(add(5,3))