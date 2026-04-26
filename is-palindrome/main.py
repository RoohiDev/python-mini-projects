# Function to check if a string is palindrome
# Palindrome: reads the same forwards and backwards (e.g., "radar", "madam")
def is_palindrome(s):
    # lower() ignores case differences (so "Radar" = "radar")
    # [::-1] reverses the string
    return s.lower() == s[::-1]

# Get input from user
user_input = input("Enter your string to check: ")

# Check and display result
if is_palindrome(user_input):
    print("Yes")  # It's a palindrome
else:
    print("No")   # Not a palindrome