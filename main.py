from math import e

LIMIT: int = 15
print(f"This program finds Euler's number up to the nth decimal place where n is at most {LIMIT}.")

EULER: str = str(e)

prompt: str = 'Enter the number of decimal places: '

user_input: str = input(prompt)

if user_input.isnumeric():
    n: int = int(user_input)
    while n > LIMIT:
        user_input = input(prompt)
        if user_input.isnumeric():
            n = int(user_input)
        else:
            break

while not user_input.isnumeric():
    user_input = input(prompt)
    if user_input.isnumeric():
        n: int = int(user_input)
        while n > LIMIT:
            user_input = input(prompt)
            if user_input.isnumeric():
                n = int(user_input)
            else:
                break

print(f"Euler's number to the {n}th decimal place is {EULER[:n+2]}")
