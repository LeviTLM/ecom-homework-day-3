import random

list_a = [random.choice([False, True]) for _ in range(3)]
print("List a:", list_a)

print("All elements are True in list a:", all(list_a))
print("At least one True in list a:", any(list_a))
print("All elements are False in list a:", all(not x for x in list_a))
print("At least one False in list a:", any(not x for x in list_a))

list_b = [random.randint(-2, 2) for _ in range(5)]
print("List b:", list_b)

print("All elements are non-zero in list b:", all(x != 0 for x in list_b))
print("At least one non-zero element in list b:", any(x != 0 for x in list_b))
print("All elements are 0 in list b:", all(x == 0 for x in list_b))
print("At least one element is 0 in list b:", any(x == 0 for x in list_b))