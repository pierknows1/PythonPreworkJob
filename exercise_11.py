# Read required string
# ====================

# 1. Use a loop to confirm that the user-entered
# `value` variable is not blank (all whitespace) or empty.
# (Hint: use the `strip` method.)
# If `value` is blank or empty, display an error message
# and re-prompt the user (re-loop).

while True:
    value = input("This value is required: ")

    if value.strip():
        break
    else:
        print('Error: Please enter a value')