from time import sleep
from os import system, name

# Function to clear screen based on OS
def clear_screen():
    if name == "nt":  # Windows
        system("cls")
    else:  # Mac/Linux
        system("clear")

print("\nWelcome To Timer Program\n")

while True:
    choice = input("Do you want to start timer? [Y/N]: ").upper()
    
    if 'Y' in choice:
        try:
            # Get time input from user
            hours = int(input("Enter hour: "))
            minutes = int(input("Enter minutes: "))
            seconds = int(input("Enter seconds: "))
            
            # Validate inputs (no negative numbers)
            if hours < 0 or minutes < 0 or seconds < 0:
                print("Time values cannot be negative!\n")
                continue
            
            # Calculate total seconds
            total = hours * 3600 + minutes * 60 + seconds
            
            # Check if timer is zero
            if total == 0:
                print("Timer is zero! Nothing to count.\n")
                continue
            
            print("\nTimer starts now...")
            sleep(1)
            
            # Countdown loop
            while total > 0:
                clear_screen()  # Clear screen each second
                print(f"\nTime remaining: {total} seconds\n")
                total -= 1
                sleep(1)
            
            # Final clear and message
            clear_screen()
            print("\n>>> TIMER ENDED! <<<\n")
            
        except ValueError:
            print("Please enter valid numbers!\n")
            
    elif 'N' in choice:
        print("\nProgram Closed.")
        break
        
    else:
        print("Invalid input! Try again.\n")