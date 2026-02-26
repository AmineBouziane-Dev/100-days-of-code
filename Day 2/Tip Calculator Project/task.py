print("Welcome to the tip calculator!")
Bill = float(input("What was the total bill? $")) #need exact number so float is perfect here
Tip_Percentage = int(input("What percentage tip would you like to give(10%,12%,20% etc)? %")) #Put int here to make sure we get a whole number not decimal but can use float
Final_Tip=(Bill*(Tip_Percentage/100))
people = int(input("How many people to split the bill? "))

Total_bill =((Bill+Final_Tip)/people)
print(f"Each Person should pay: ${round(Total_bill, 2)}")
