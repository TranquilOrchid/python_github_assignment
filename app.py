# Simple Study Time Tracker
# Task 1: welcome message

print("Welcome to my Python program!")

hours = input("How many hours did you study today? ")

# Convert input to a number
hours = float(hours)

# Calculate weekly total
weekly_hours = hours * 7

# Display the result
print(f"You are on track to study {weekly_hours} hours this week.")