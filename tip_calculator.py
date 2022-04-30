
#Greeting the users
print("Welcome to ahmed's tip calculator!")
#Promt for bill total
total_bill = float(input("what was the total bill? "))
#promt for tip
tip = int(input("how much tip would you like to give? 10,12, or 15? "))
#promt for amount of people
people = int(input("how many people will split the bill? "))
#Calcualtion
tip_percent = (tip/100)+1 
money_each = (total_bill/people)*tip_percent
rounded_money = round(money_each,2)
rounded_money = "{:.2f}".format(money_each)
print(f"Each person should pay: {rounded_money}")