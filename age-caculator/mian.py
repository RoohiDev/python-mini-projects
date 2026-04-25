# importing datetime module to get current year
from datetime import datetime

# get current year from system
current_year = datetime.now().year

# get user's birth year and convert string to integer
birth_year = int(input("Enter your birth date year: "))

# calculate age by subtracting birth year from current year
user_age = current_year - birth_year

# show result to user
print(f"You are {user_age} years old.")