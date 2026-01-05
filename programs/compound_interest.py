princ = int(input("Enter the principal amount: "))
while princ < 0:
    print("Principal amount can't be smaller than 0")
    princ = int(input("Enter the principal amount: "))

interest = int(input("Enter the interest rate:"))
while interest < 0:
    print("Interest rate can't be smaller than 0")
    interest = int(input("Enter the interest rate: "))

time = int(input("Enter the duration(in years): "))
while time < 0:
    print("Time can't be smaller than 0")
    time = int(input("Enter the duration(in years): "))

total = princ * pow((1+interest/100), time)

print(f"The total amount after {time} year will be {round(total)}")