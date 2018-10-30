total_cost = float(input("Enter the cost of your dream home: "))
print("dream home price " + str(total_cost))

annual_salary = float(input("Enter your annual salary: "))
print("how much you make " + str(annual_salary))

portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
print("portion saved each month " + str(portion_saved) + "%")

portion_down_payment = 0.25
total_down_payment = (total_cost * portion_down_payment)
print("the total down payment " + str(total_down_payment))

current_savings = 0
r = 0.04
monthly_savings = (annual_salary / 12) * portion_saved
print("you would save " + str(monthly_savings) + "each month")
months_to_make_down_payment = 0

while (total_down_payment >= current_savings):
    monthly_savings += monthly_savings * (r / 12)
    current_savings += monthly_savings
    months_to_make_down_payment += 1
print(str(months_to_make_down_payment) + " months that you need to save for")
