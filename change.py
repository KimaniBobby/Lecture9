#change.py
#A program to claculate the value of some change in dollars

def main():
    print("Change Counter")
    print()
    print("Please enter the print count of each coin type.")
    
    quarters = int(input("Quarters:"))
    
    dimes = int(input("Dimes:"))
    
    nickels = int(input("Nickels:"))
    
    pennies = int(input("Pennies:"))

    total = quarters * 0.25 + dimes* 0.10+ nickels * 0.05+ pennies* 0.01

    print()

    print("The total value of your change is: ",total)

main()
