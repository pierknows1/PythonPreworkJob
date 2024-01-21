# message = "Visit Mars."
# index = 0

# while index < len(message):
#     print(message[index])
#     index += 1  # or index += 1


# import random

# a = 1
# b = 2
# c = 3

# while a < 50 or b % 2 == 0 and c % 3 != 0:
#     print(f"{a},{b},{c}")

#     a = random.randrange(100)
#     b = random.randrange(100)
#     c = random.randrange(100)

#     word = ""

# while word != "magic":
#     word = input('Enter the "magic" word: ')

# print("You got it!")

# # for individual_item in sequence:
# #     pass

# word = "Looping..."

# for char in word:
#     print(char)

# sum = 0
# # sum the numbers less than or equal to 10
# for n in range(11):
#     sum += n

# print(f"Sum: {sum}") 

print("Countdown:")
for i in range(10, 0, -1):
    print(i)

print("Blast off!")

for i in range(4, 100, 5):
    print(i)


    message = "Grouper, Halibut, and Trout"
vowels = "aeiou"
result = ""
# remove all vowels from `message` and store the new string in `result`
for i in range(len(message)):
    if vowels.find(message[i]) < 0:
        result += message[i]

print(f"Result: {result}")  # Result: Grpr, Hlbt, nd Trt

message = "Grouper, Halibut, and Trout"
vowels = "aeiou"
result = ""
# remove all vowels from `message` and store the new string in `result`
for char in message:
    if vowels.find(char) < 0:
        result += char

print(f"Result: {result}")  # Result: Grpr, Hlbt, nd Trt

import random

for i in range(10000):
    print(f"First line in the block: {i}")

    # a 10% chance to break out of the loop
    if random.random() > 0.9:
        print("breaking!")
        break  # exit the for's code block immediately

    print(f"Last line in the block: {i}")


    value = ""
one_through_five = "12345"

while True:
    value = input("Enter 1-5: ")
    if len(value) == 1 and one_through_five.find(value) >= 0:
        break

value = ""
one_through_five = "12345"
is_valid = False

while not is_valid:
    value = input("Enter 1-5: ")
    if len(value) == 1 and one_through_five.find(value) >= 0:
        is_valid = True


import random

# print all even numbers under 100
n = 0
while n < 100:
    if n % 2 == 1:
        n += 1
        continue  # skip remaining code, but continue looping

    print(n)
    n += 1

# print 20% of the numbers under 100, randomly
for n in range(100):
    if random.random() < 0.80:
        continue  # skip remaining code, but continue looping

    print(f"lucky number: {n}")
