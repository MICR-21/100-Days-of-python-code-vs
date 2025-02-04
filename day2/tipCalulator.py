print("Welcome to the tip Calculator")
bill = float((input("What was the total bill?$ ")))
tip = float(input("How much tip would you like to give? 10, 12, or 15? "))
people = int((input("How may people split the bill? ")))
tip_bill = round(tip/100*bill + bill, 2)
bill_person=tip_bill/people
print(f"Each person should pay: ${bill_person}")