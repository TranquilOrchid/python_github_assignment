# Simple Study Time Tracker
# Task 1: welcome message

print("Welcome to my Python program!")

hours = input("How many hours did you study today? ")

# Convert input to a number
hours = float(hours)

# Try to convert input to a number
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()

# Calculate weekly total
weekly_hours = hours * 7

# Display the result
print(f"You are on track to study {weekly_hours} hours this week.")