import random

a = 1
b = 2
c = 3

while a < 50 or b % 2 == 0 and c % 3 != 0:
    print(f"{a},{b},{c}")

    a = random.randrange(100)
    b = random.randrange(100)
    c = random.randrange(100)
