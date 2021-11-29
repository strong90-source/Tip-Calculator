#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
howMuchTip = int(input("How much tip would you like to give? 10, 12 or 15? "))
howManyPeople = int(input("How many people to split the bill?"))
bill_with_tip = howMuchTip / 100 * bill + bill
total_bill = bill_with_tip / howManyPeople
total_final = round(total_bill, 2)
total_final = "{:.2f}".format(total_bill)
print(f"Each person should pay: ${total_final}")


