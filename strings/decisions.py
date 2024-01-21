# # Anatomy of an if statement
# # if bool-expression:
# #     pass
# # ^   ^       ^     ^
# # |   |       |     |
# # |   |       |     |
# # |   |       |     |
# # |   |       |   colon
# # |   |       |
# # |   |    boolean expression, condition
# # |   |
# # |  code block (indent)
# # |
# # if keyword

# if True:
#     print("It's true.")  # the expression is True so this runs

# if False:
#     print("It's true.")  # the expression is False so this doesn't run


# value = 1.000
# print(type(value))  # <class 'NoneType'>


# package_weight = 0.55

# if package_weight > 100.0:  # check first condition
#     print("too big for standard shipping")
# elif package_weight < 1.0:  # check a second condition
#     print("too small. send a letter.")
# else:  # the `else` clause executes if all other conditions are False.
#     print("can ship")


# package_weight = 0.55

# if package_weight > 100.0:  # check first condition
#     print("too big for standard shipping")
# else:
#     if package_weight < 1.0:  # check a second condition
#         print("too small. send a letter.")
#     else:  # the `else` clause executes if all other conditions are False.
#         print("can ship")

# color = "orange"

# if color == "red":
#     print("red's compliment is green")
# elif color == "blue":
#     print("blue's compliment is orange")
# elif color == "yellow":
#     print("yellow's compliment is purple")
# elif color == "green":
#     print("green's compliment is red")
# elif color == "orange":
#     print("orange's compliment is blue")
# elif color == "purple":
#     print("purple's compliment is yellow")
# else:
#     print("I don't know that color")



place = 2
ribbon_color = None

# 1. match keyword, then an expression (often a variable), followed by a colon, `:`
match place:
    case 1:  # 2. case keyword, then a literal value, then colon.
        # if the switch's expression resolves to the case's value,
        # all code nested inside the case executes.
        ribbon_color = "blue"
        print("first place!")
    case 2:
        ribbon_color = "red"
        print("second place!")
    case 3:
        ribbon_color = "white"
        print("third place!")
    case _:  # 3. underscore, _, is a default case, happens when no other case matched
        ribbon_color = "unknown"

print(ribbon_color)

color = input("Choose a color: ").strip().lower()

match color:
    case "red" | "yellow" | "blue":
        print("primary color")
    case "green" | "purple" | "orange":
        print("secondary color")
    case _:
        print("regular color")
