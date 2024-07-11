
score = int(input("Enter your test score: "))


if score < 0 or score > 100:
    print("ilegall grade!")
elif score <= 40:
    print("try harder next time...")
elif score <= 60:
    print("you're getting there, need some more work")
elif score <= 80:
    print("good job!")
elif score <= 95:
    print("awesome!")
else:
    print("excellent!!! You're a Star!")