print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?: $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
percentage = (tip / 100) + 1
people = int(input("How many people to split the bill? "))
total = round((bill / people) * percentage, 3)
print(f"Each person should pay: {total}")
