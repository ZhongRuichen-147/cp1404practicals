"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
   When the user enters input that cannot be converted to an integer (e.g., blank, 3.5)
2. When will a ZeroDivisionError occur?
   When the denominator is 0 and the program attempts to divide by it.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   Yes, Validate the denominator and keep asking unti it is not zero, so division is never attempted with 0.
"""

is_valid = False

while not is_valid:
    try:
        numerator = int(input("Enter the numerator: "))
        is_valid = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")

is_valid = False
while not is_valid:
    try:
        denominator = int(input("Enter the denominator: "))
        if denominator == 0:
            print("Denominator cannot be zero!")
        else:
            is_valid = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")

fractions = numerator / denominator
print(fractions)
print("Finished.")