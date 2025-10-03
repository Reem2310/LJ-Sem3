# Write a Python Program to calculate the sum of three given numbers, if the values are equal then return thrice their sum. 

num1=int(input("Enter the number 1 : "))
num2=int(input("Enter the number 2 : "))
num3=int(input("Enter the number 3 : "))
if num1 == num2 or num2 == num3:
    res=(num1+num2+num3)*3
    print(f"All numbers are equal. Thrice their sum is: {res}")
else:
    res=num1+num2+num3
    print(f"The sum of the numbers is: {res}")