numbers_list = [1, 2, 3, 4]

while True:
    try:
        user_input = input("Enter an index (or -999 to stop): ")

        if user_input == "-999":
            break

        index = int(user_input)

        if index < 0 or index >= len(numbers_list):
            raise IndexError("Index is out of range.")

        print("Element at index", index, ":", numbers_list[index])

    except ValueError:
        print("Invalid input Please enter a valid number.")

    except IndexError as e:
        print("Error:", e)

    except Exception as e:
        print("An error occurred:", e)