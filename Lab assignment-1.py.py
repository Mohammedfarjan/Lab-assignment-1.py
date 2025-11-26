print("Welcome to the Calorie Meter!")
print("Track your meals' calories and compare against your daily limit.")

meals = []
calories = []

num_meals = int(input("Enter the number of meals you've taken: "))

for i in range(num_meals):
    meal_name = input(f"Enter {i+1}th meal's name: ")
    cal = float(input(f"Enter calories for {meal_name}: "))
    meals.append(meal_name)
    calories.append(cal)  # corrected variable name

total_calories = sum(calories)
avg_calories = total_calories / num_meals

daily_limit = float(input("Enter your daily calorie limit: "))

print("\nSummary:")
for i in range(num_meals):
    print(f"{meals[i]}: {calories[i]} calories")

print(f"\nTotal Calories: {total_calories}")
print(f"Average Calories per Meal: {avg_calories}")
print(f"Daily Limit: {daily_limit}")

if total_calories > daily_limit:
    print(f"Warning: You've exceeded your daily calorie limit by {total_calories - daily_limit} calories.")
else:
    print(f"You've got {daily_limit - total_calories} calories 