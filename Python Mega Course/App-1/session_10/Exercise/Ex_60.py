# Percentage Calculator with Error Handling
# Take a look at the code in the coding area. You should expand that code. Your task is to:

# (1) calculate the percentage using the  value/total * 100 formula
# (2) print out the message "That is 40.0%" (or whatever the calculated percentage value is)
# (3) If the user doesn't enter a number but a string (e.g., hi) for the total value or the value, the program should print out the message shown in the screenshot below:

try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))
    percentage = value / total_value * 100
    print(f"That is {percentage:.1f}%")
except ValueError:
    print("You need to enter a number. Run the program again.")