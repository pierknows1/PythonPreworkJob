quote = """The human world is made of stories, not people.
The people the stories use to tell themselves are not to be blamed."""
# -- David Mitchell, Ghostwritten

# print(quote[4:9])  # human


print('=' * 15)
# print(quote[0:10])
# print(quote[10:15])
# print(quote[27:34])
# print(quote[34:35])
# print(quote[40:46])
# print(quote[48:51])
# print(quote[102:115])


words=[(0,10), (10,15), (27,34), (34,35), (40,46), (48,51), (102,115)]

for start, end in words:
    print(quote[start:end])

# 1. Use string slicing to print a substring
# from `quote` to the terminal.
#
# Expected output:
# ================
# The human
# world
# stories
# ,
# people
# The
# to be blamed.
