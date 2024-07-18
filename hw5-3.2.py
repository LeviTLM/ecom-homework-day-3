def star_wars(base):
    for i in range(1, base + 1, 2):
        print(' ' * ((base - i) // 2) + '*' * i)



def get_odd_positive_number():
    while True:
        try:
            num = int(input("Enter a positive odd number greater than 0: "))
            if num > 0 and num % 2 != 0:
                return num
            else:
                print("Please enter a positive odd number.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    base = get_odd_positive_number()
    star_wars(base)