import random

line_number = 6
minimum = 1
maximum = 45

quick_pick = int(input("How many quick picks? "))
while quick_pick <= 0:
    print("Input error")
    quick_pick = int(input("How many quick picks? "))

for i in range(quick_pick):
    quick_picks = []
    for j in range(line_number):
        number = random.randint(minimum, maximum)
        quick_picks.append(number)

    quick_picks.sort()
    numbers = ' '.join(f"{number:2}" for number in quick_picks)
    print(numbers)
