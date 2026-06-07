# Define intensity function
def get_intensity(cal_rate):
    if cal_rate >= 10:
        return "High"
    elif cal_rate >= 5:
        return "Medium"
    else:
        return "Low"

# Define calories per minute function
def calories_per_minute(calories, duration):
    return round(calories / duration, 2)

# Greet the user and explain the program
print("Welcome to the Personal Fitness Tracker!")
print("You will log 3 workouts.")

# use a for loop that runs exactly 3 times
for i in range(1, 4):
    print(f"\n=== Workout {i} ===")

    # Collect user input
    name = input("Workout name: ")
    duration = int(input("Duration (in minutes): "))
    calories = int(input("Calories burned: "))

    # store all three values for that workout in a list
    workout_data = [name, duration, calories]

    # call the functions using the values from the list
    # workout_data[0] = name, workout_data[1] = duration, workout_data[2] = calories
    cal_rate = calories_per_minute(workout_data[2], workout_data[1])
    intensity = get_intensity(cal_rate)

    # immediately print a formatted summary line
    print(f"Result: {workout_data[0]} | {workout_data[1]} min | {workout_data[2]} cal |{cal_rate} cal/min | Intensity: {intensity}")

#after the loop ends print a closing message
print("\nAll workouts logged. Great Job staying active!")
