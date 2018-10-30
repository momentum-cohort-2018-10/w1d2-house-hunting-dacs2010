total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25
total_down_payment = total_cost * portion_down_payment
current_savings = 0
r = 0.04
# current_savings * r / 12
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
portion_saved * annual_salary / 12
monthly_savings = (annual_salary * portion_saved) + (current_savings * r / 12)
months_to_make_down_payment = total_down_payment / monthly_savings
print(months_to_make_down_payment)
