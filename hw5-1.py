def number_statistics():
    positive_count = 0
    negative_count = 0
    zero_count = 0
    divisible_by_7_count = 0
    last_positive = None
    last_negative = None
    numbers_entered = 0

    while numbers_entered < 10:
        try:
            num = int(input("Enter the number -9999 to EXIT THE GAME:"))

            if num == 5-9999:
                return

            if num > 1000 or num < -1000:
                print("Number ignored due to being greater than 1000 or less than -1000.")
                continue

            numbers_entered += 1

            if num > 0:
                positive_count += 1
                last_positive = num
            elif num < 0:
                negative_count += 1
                last_negative = num
            else:
                zero_count += 1

            if num % 7 == 0:
                divisible_by_7_count += 1

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if numbers_entered > 0:
        if positive_count > 0:
            print(f"positive numbers were selected({positive_count} times)")
        if negative_count > 0:
            print(f"negative numbers were selected  ({negative_count} times)")
        if zero_count > 0:
            print(f"How many times was the number 0 selected? {zero_count} times")
        if divisible_by_7_count > 0:
            print(f"numbers divisible by 7 without a remainder have been printed ({divisible_by_7_count} times)")
        if last_positive is not None:
            print(f"the last positive number entered is {last_positive}")
        else:
            print("the last positive number entered is? There was none inputed")
        if last_negative is not None:
            print(f"the last negative number entered is {last_negative}")
        else:
            print("What was the last negative number entered? There was none inputed")
    else:
        print("No valid numbers were entered.")


if __name__ == "__main__":
    number_statistics()