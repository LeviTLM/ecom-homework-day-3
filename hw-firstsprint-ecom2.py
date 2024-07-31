def display_numbers(top):
    for i in range(1, top + 1):
        print(i)

def display_range(num1, num2):
    start = min(num1, num2)
    end = max(num1, num2)
    for i in range(start, end + 1):
        print(i)

def display_even_numbers(n):
    for i in range(0, n + 1, 2):
        print(i)

def display_divisibles(max_val, den):
    for i in range(den, max_val + 1, den):
        print(i)

top = int(input("Enter a natural number: "))
display_numbers(top)

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
display_range(num1, num2)

n = int(input("Enter a natural number: "))
display_even_numbers(n)

max_val = int(input("Enter the maximum number: "))
den = int(input("Enter the denominator: "))
display_divisibles(max_val, den)