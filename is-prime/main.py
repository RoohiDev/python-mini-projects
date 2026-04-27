# Function to check if a number is prime using for-else
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    else:
        # This runs only if loop completed without break/return
        return True

# Get user input with error handling
try:
    user_input = int(input("Enter your number: "))
except ValueError:
    print("Please enter a numeric value!")
    exit()

# Check and display result
if user_input < 2:
    print(f"{user_input} is neither prime nor composite")
elif is_prime(user_input):
    print(f"{user_input} is prime")
else:
    print(f"{user_input} is composite")