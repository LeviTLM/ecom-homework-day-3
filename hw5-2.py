import random


def guessing_game():

    lucky_number = random.randint(1, 100)

    print("Welcome to the guessing game!!")
    print("Draw a lucky number between 1-100...")


    guessed = False
    tries = 0


    while not guessed:

        guess = int(input("Enter a number between 1 and 100: "))


        tries += 1

        if guess > lucky_number:
            print("your number is too big")
        elif guess < lucky_number:
            print("your number is too small")
        else:
            print("BINGO!")
            guessed = True


    print(f"You guessed the number in {tries} tries.")
    print(f"The lucky number was: {lucky_number}")



play_again = True
while play_again:
    guessing_game()
    play_again_input = input("Do you want to play again? (yes/no): ").lower()
    play_again = play_again_input == "yes"

print("Thanks for playing!")