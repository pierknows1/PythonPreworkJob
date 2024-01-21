# Accumulate
# ==========

sum = 0

while True:
    value = input('Enter a number or "done": ')

    if value.lower() == "done":
        break

    try:
        num = int(value)
        sum += num
        print(f"Value is {num}. Sum is {sum}.")
    except ValueError:
        print("Error: Please enter a valid number or 'done'.")

# 1. Use a loop to accumulate a `sum`.
# If the user enters "done", exit the loop.
# If they don't, assume the value is a number and convert
# it to an int, adding it to `sum`. Re-loop.
# Print both the user-entered int and the `sum` in each loop.

# Example
# ================
# Enter a number or "done": 3
# Value is 3. Sum is 3.
# Enter a number or "done": 9
# Value is 9. Sum is 12.
# Enter a number or "done": -2
# Value is -2. Sum is 10.
# Enter a number or "done": 25
# Value is 25. Sum is 35.
# Enter a number or "done": done
