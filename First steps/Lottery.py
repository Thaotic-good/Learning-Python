import random

picks = set()

while len(picks) < 8:
    numbers = random.randrange(1, 51)
    picks.add(numbers)

print(picks)
