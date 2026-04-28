# Import random number generator
from random import randint

# Game settings
n = 50  # Maximum number (0 to 50)
target = randint(0, n)  # Random target number
attempts = 0  # Counter for user guesses

print('Welcome to "Guess The Number"\n')

# Main game loop
while True:
    # Get user input with validation
    try:
        userTarget = int(input(f"Enter your target number (0-{n}): "))
    except ValueError:
        print(f"Enter a numeric value (0-{n})")
        continue
    
    # Check if number is in range
    if userTarget < 0 or userTarget > n:
        print(f"Enter a number between 0 and {n}")
        continue
    
    # Count this attempt
    attempts += 1
    
    # Check guess
    if userTarget == target:
        print(f"You Win! Your attempts: {attempts}")
        break  # Exit loop when won
    elif userTarget > target:
        print("It's bigger! go down!")
    else:
        print("It's lower! go up!")