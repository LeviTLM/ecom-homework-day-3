def print_smallest_three_times(num1, num2):
    smallest = min(num1, num2)
    print(smallest * 3)

def print_average(num1, num2):
    average = (num1 + num2) / 2
    print("Average:", average)

def print_largest(num1, num2, num3):
    largest = max(num1, num2, num3)
    print("Largest number:", largest)

def print_movie_length(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    print(f"{hours} hour(s) and {remaining_minutes} minute(s)")

def print_rightmost_digit(number):
    rightmost_digit = number % 10
    print("Rightmost digit:", rightmost_digit)

def print_second_digit(number):
    second_digit = (number // 10) % 10
    print("Second digit from the right:", second_digit)

def sum_of_digits(number):
    tens = number // 10
    units = number % 10
    total = tens + units
    print("Sum of digits:", total)

def reverse_digits(number):
    tens = number // 10
    units = number % 10
    reversed_number = units * 10 + tens
    print("Reversed number:", reversed_number)

def check_even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

def calculate_tax(salary):
    tax = 0
    if salary > 50000:
        tax += (salary - 50000) * 0.51
        salary = 50000
    if salary > 35000:
        tax += (salary - 35000) * 0.45
        salary = 35000
    if salary > 25000:
        tax += (salary - 25000) * 0.40
        salary = 25000
    if salary > 18000:
        tax += (salary - 18000) * 0.30
        salary = 18000
    if salary > 12000:
        tax += (salary - 12000) * 0.20
        salary = 12000
    if salary > 6000:
        tax += (salary - 6000) * 0.10
    print("Total tax to be paid:", tax)

def check_roller_coaster(age, height):
    if age <= 18:
        if height > 115:
            print("Allowed to board the roller coaster.")
        else:
            print("Not allowed to board the roller coaster.")
    else:
        if height > 100:
            print("Allowed to board the roller coaster.")
        else:
            print("Not allowed to board the roller coaster.")

num1 = float(input("Enter first decimal number: "))
num2 = float(input("Enter second decimal number: "))
print_smallest_three_times(num1, num2)

num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
print_average(num1, num2)

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
print_largest(num1, num2, num3)

minutes = int(input("Enter movie length in minutes: "))
print_movie_length(minutes)

number = int(input("Enter a 4-digit number: "))
print_rightmost_digit(number)
print_second_digit(number)

number = int(input("Enter a two-digit number: "))
sum_of_digits(number)
reverse_digits(number)

number = int(input("Enter a number: "))
check_even_odd(number)

salary = float(input("Enter your salary: "))
calculate_tax(salary)

age = int(input("Enter age: "))
height = int(input("Enter height in cm: "))
check_roller_coaster(age, height)