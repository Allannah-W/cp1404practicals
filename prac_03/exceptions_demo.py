"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When a non-integer value is entered as an input
2. When will a ZeroDivisionError occur?
When a 0 is entered as an input for the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
By preventing the denominator input from being 0
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
