import random

list_a = list(range(95, 106))
print("List a:", list_a)

list_b = list(range(10, 21, 2))
print("List b:", list_b)

list_c = [random.choice([False, True]) for _ in range(5)]
print("List c:", list_c)

list_e = [random.randint(1, 100) for _ in range(10)]
print("List d:", list_e)

list_f = [x for x in list_e if x > 50]
print("List e (numbers greater than 50):", list_f)

list_e, list_f = [random.randint(1, 100) for _ in range(10)], [x for x in list_e if x > 50]
print("List f (random numbers):", list_e)
print("List g (numbers greater than 50):", list_f)

user_input = "hello python masters"
filtered_letters = [char for char in user_input if char != 't' and not char.isspace()]
print("Filtered letters:", filtered_letters)