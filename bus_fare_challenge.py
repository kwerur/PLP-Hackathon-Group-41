from datetime import datetime
import calendar
# Bus Fare calculation
date = datetime.now()
print("Date: ", date.date())
exact_day = calendar.day_name[date.weekday()].capitalize()
print("Day: ", exact_day)
if exact_day.lower() == "saturday":
    print("Fare: ", 60)
elif exact_day.lower() == "sunday":
    print("Fare: ", 80)
else:
    print("Fare: ", 100)
