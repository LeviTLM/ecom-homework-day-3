def temperature_data():
    temps = []
    for _ in range(12):
        while True:
            try:
                temp = float(input())
                if 5 <= temp <= 40:
                    if temps and temps[-1] == 0 and temp == 0:
                        print("Error: Consecutive zeros. Enter the temperature again.")
                        continue
                    temps.append(temp)
                    break
                else:
                    print("data wrong")
                    return
            except ValueError:
                print("data wrong")
                return
    avg_temp = sum(temps) / len(temps)
    print(f"Annual Average Temperature: {avg_temp}")
    print(f"Highest Temperature: {max(temps)}")
    print(f"Lowest Temperature: {min(temps)}")


def voting_system():
    votes = []
    for i in range(1, 45):
        while True:
            try:
                vote = int(input())
                if 1 <= vote <= 4:
                    votes.append(vote)
                    if vote == 4:
                        print(f"Veto by country {i}")
                        return
                    break
                else:
                    print("Invalid code. Enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Enter a number between 1 and 4.")

    in_favor = votes.count(1)
    against = votes.count(2)
    abstained = votes.count(3)

    print(f"Votes in favor: {in_favor}")
    print(f"Votes against: {against}")
    print(f"Votes abstained: {abstained}")

    first_favor = next((i + 1 for i, v in enumerate(votes) if v == 1), None)
    last_against = next((i + 1 for i, v in reversed(list(enumerate(votes))) if v == 2), None)

    print(f"First country voting in favor: {first_favor if first_favor else 'None'}")
    print(f"Last country voting against: {last_against if last_against else 'None'}")

# temperature_data()
# voting_system()


