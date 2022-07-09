print("This is a Painting Job Cost Evaluation program")
area = float(input("Enter the area of the wall in square feet "))
number_of_gallons = round((area / 115), 2)
labour_hours = round(((area / 115) * 8), 2)
labour_cost = round((labour_hours * 20), 2)
cost_per_paint_gallon = float(input("How much does 1 gallon of paint cost? $"))
paint_cost = round((number_of_gallons * cost_per_paint_gallon), 2)
total_cost = round((paint_cost + labour_cost), 2)

print(f"\nYour {area} Square feet will require the following:\n")
print("Number of gallons of paint required ", number_of_gallons)
print("Hours of labor required ", labour_hours)
print("Cost of the paint $", paint_cost)
print("Labor charges $", labour_cost)
print("Total cost of the paint job $", total_cost)
