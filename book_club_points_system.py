def greeting(name):
    print("Greetings, ", name, "\nWelcome to our points awarding programme")


print("\nWelcome to the Book Club Points Serendipity Booksellers")
customer_name = input("What is your name? ")

greeting(customer_name)

books_purchased = int(input("How many books have you purchased this month? "))

if books_purchased < 1:
    points = 0
elif books_purchased == 1:
    points = 6
elif books_purchased == 2:
    points = 16
elif books_purchased == 3:
    points = 32
elif books_purchased == 4:
    points = 60
elif books_purchased > 4:
    print("Eish! Are you sure... Okay, anyway the maximum awards per person per month is 60 points :)")
    points = 60
else:
    print("Invalid entry")
print("You have been awarded ", points, " points")

