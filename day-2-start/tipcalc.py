#Welcome to the tip calculator
#What was the total bill? $124.56
#What percentage tip would you like to give? 10, 12, or 15? 12
#How many people to split the bill? 7
#Each person should pay: $19.93

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10. 12. or 15?"))
people = int(input("How many people to split the bill?"))
bill_with_tip = tip /100 * bill + bill
print(bill_with_tip)