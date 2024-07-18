def number_printer(n):

    for i in range(1, n + 1):
        print(''.join(str(x) for x in range(1, i + 1)))

    for i in range(n - 1, 0, -1):
        print(''.join(str(x) for x in range(1, i + 1)))

def get_positive_integer():
    while True:
        try:
            num = int(input("Enter a positive integer greater than 0: "))
            if num > 0:
                return num
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    num = get_positive_integer()
    number_printer(num)