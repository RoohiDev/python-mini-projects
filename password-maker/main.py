# Import sample for random selection without repeats
from random import sample
# Import ascii_letters for A-Z and a-z
from string import ascii_letters

# Character sets for password generation
letters = ascii_letters  # Uppercase and lowercase letters
symbols = '!"@#$%^&*()_+=<>-?'  # Special characters
numbers = "0123456789"  # Digits 0-9
all_chars = letters + symbols + numbers  # Combine all characters

print("\n========= Welcome To Password Maker Program =========\n")

# Main program loop
while True:
    # Show menu and get user choice
    choice = input("Select Option: \n\t1) Create Password\n\t2) Exit\nYour Option: ")
    
    if choice == "1":
        try:
            # Get desired password length
            length = int(input("Enter your password length: "))
            
            # Check if length is positive
            if length <= 0:
                print("\nPassword length must be greater than 0!\n")
                continue
            
            # Check if enough characters available
            if length > len(all_chars):
                print(f"\nMaximum password length is {len(all_chars)} (not enough characters)\n")
                continue
            
            # Generate password: sample picks unique chars, join combines them
            password = "".join(sample(all_chars, length))
            
            # Display the generated password
            print("\n" + f"Your password: {password}")
            print("\n"+ "=" * 53 + "\n")
            
        except ValueError:
            # Handle non-numeric input
            print("\nPlease enter a valid number!\n")
            
    elif choice == "2":
        # Exit the program
        print("\nProgram Closed")
        break
        
    else:
        # Handle invalid menu option
        print("\nInvalid input! Try again")
        print("\n" + "=" * 53 + "\n")