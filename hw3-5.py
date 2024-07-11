number = int(input("Enter an integer: "))

if number % 5 == 0 and number % 3 == 0:
    print("Buzz Fizz")
elif number % 5 == 0:
    print("Fizz")
elif number % 3 == 0:
    print("Buzz")
else:
    print(number)