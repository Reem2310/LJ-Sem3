# Leap Year Checking with Examples

# Divisible by 4
# Example: 2024 ÷ 4 = 506 → divisible → possible leap year.
# Example: 2023 ÷ 4 = 505 remainder 3 → not divisible → NOT a leap year.

# Divisible by 100 (century years)
# Example: 1900 ÷ 100 = 19 → divisible by 100 → normally NOT a leap year.
# Example: 2000 ÷ 100 = 20 → divisible by 100 → check next rule.

# Divisible by 400 (special case for century years)
# Example: 2000 ÷ 400 = 5 → divisible → ✅ Leap year.
# Example: 2100 ÷ 400 = 5 remainder 100 → not divisible → ❌ NOT a leap year.

year=int(input("Enter the year:"))
if year % 4==0:
    if year % 100 ==0:
        if year % 400 ==0:
            print("The year is Leap")
        else:
            print("The year is not Leap")
    else:
        print("The year is Leap")
else:
    print("The year is not Leap")