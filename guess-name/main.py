from random import choice
from time import sleep

# List of names (computer guesses from this list)
names = ['Alice', 'Bob', 'Gabriel', 'James', 'Juan', 'Alex', 'Paul', 'Tony', 'Eliot', 'Jessie', 'Diana']
names_cp = names.copy()  # Copy to remove guessed names

print("Choose one of these names in your mind:")
print(names)
sleep(3)  # Give user time to think

# Main game loop
while True:
    # If no names left, user's name wasn't in list
    if len(names_cp) == 0:
        print("\nI couldn't guess your name! Is it not in the list?")
        break
    
    # Computer guesses a random name from remaining list
    bot_guess = choice(names_cp)
    
    # Input validation loop
    while True:
        question = input(f"\nIs your name {bot_guess}? [Y/N]: ").strip().upper()
        
        if not question:  # Empty input
            print("Please enter something! Type Y or N")
            continue
            
        if question not in ['Y', 'N', 'YES', 'NO']:
            print("Invalid input! Please enter Y (yes) or N (no)")
            continue
            
        break  # Valid input received
    
    # Check answer
    if question in ['Y', 'YES']:
        print("\nI guessed right! ^_^")
        break
    elif question in ['N', 'NO']:
        print("\nOops! +_+ let me try again")
        names_cp.remove(bot_guess)  # Remove wrong guess from list