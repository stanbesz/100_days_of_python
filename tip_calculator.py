print("Welcome to the tip calculator?")
MAX_PERCENT = 100

bill_to_pay = float(input("How much is the bill? $"))

tip_percent = int(input("What percent bill do you want? 10, 12, 15 or 20 %"))

people_to_pay = int(input("How many people will pay?"))

calculate_bill = (bill_to_pay+bill_to_pay*(tip_percent/MAX_PERCENT))/people_to_pay

print(f"Each person should pay: ${round(calculate_bill,2)}")
