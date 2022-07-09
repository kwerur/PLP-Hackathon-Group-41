from datetime import datetime
import calendar
# # date_object = datetime.now()
# # print(date_object)
# # print(type(date_object))
# my_string = "1988-05-25"
# my_date = datetime.strptime(my_string, "%Y-%m-%d")
# print(my_date, type(my_date))
#
# print("Month", my_date.month, "; Year", my_date.year, "; Date", my_date.day)
# print(my_date.weekday())
#
# print("I was born on a ", calendar.day_abbr[my_date.weekday()].capitalize())
# i = 0
# for weekday in calendar.day_name:
#     print(i, "-", weekday)
#     i += 1
#
# leo = datetime.now()
# print(leo)
#
# print(calendar.day_name[leo.weekday()].upper())
# if (calendar.day_name[leo.weekday()].upper()) == "THURSDAY":
#     print("SABA SABA!!")
# else:
#     print("WHAAAAAT!!!")
#
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