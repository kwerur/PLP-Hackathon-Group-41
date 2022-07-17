def greet(client):
    print("Hello, ", client, "\n")


# Calories calculations
print("\nWelcome to Group 41 Nutritionists, Here we calculate your calories!\n")
client_name = input("What is your name?")

greet(client_name)

carbs = int(input("How many grams of carbohydrates have you taken? "))
fats = int(input("How many grams of fats have you taken? "))

calories = (carbs * 4) + (fats * 9)

print("\nFrom your Fats consumption: ", fats * 9, " Calories")
print("From your Carbohydrates consumption: ", carbs * 4, " Calories")

print("You have consumed ", calories, " calories,", client_name)
