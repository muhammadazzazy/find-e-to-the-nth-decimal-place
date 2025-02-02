from math import e
from sys import exit

def main() -> None:
    LIMIT: int = 15
    print(f'Welcome to The ℇ Approximator!')

    EULER: str = str(e)

    prompt: str = f'Enter the number of decimal places (up to {LIMIT}): '

    while True:
        user_input: str = input(prompt)

        if user_input == 'exit':
            print('Thanks for trying my program!')
            exit()

        if not user_input.isnumeric():
            print('Please enter a whole number between 0 and 15...')
            continue
    
        n: int = int(user_input)
        print(f'ℇ to the {n}th decimal place is {EULER[:n+2]}')

main()
