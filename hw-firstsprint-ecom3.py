def sum_until_neg99():
    total = 0
    while True:
        num = int(input())
        if num == -99:
            print(None if total == 0 else total)
            return
        total += num

def min_max_until_neg_or_zero():
    values = []
    while True:
        num = int(input())
        if num <= 0:
            print(None if not values else f"Highest: {max(values)}\nLowest: {min(values)}")
            return
        values.append(num)

def serial_of_highest():
    numbers = [int(input()) for _ in range(5)]
    highest = max(numbers)
    print(numbers.index(highest) + 1)

def multiply_using_addition(a, b):
    result = 0
    for _ in range(b):
        result += a
    print(result)

def multiply_using_multiplication(a, b):
    result = 0
    for _ in range(b):
        result += a
    print(result)

def digit_in_number(number, digit):
    print(str(digit) in str(number))

def gcd(a, b):
    while b:
        a, b = b, a % b
    print(a)

def is_prime(num):
    if num <= 1:
        print(False)
        return
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(False)
            return
    print(True)


# sum_until_neg99()
# min_max_until_neg_or_zero()
# serial_of_highest()
# multiply_using_addition(5, 3)
# multiply_using_multiplication(5, 3)
# digit_in_number(789, 3)
# gcd(60, 72)
# is_prime(29)