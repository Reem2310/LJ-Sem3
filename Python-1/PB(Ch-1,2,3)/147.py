#  Write a program to find sum of first N natural numbers given by user.
n=int(input("Enter the number :"))
if n>0:
    num=(n*(n+1)/2)
    print(f"The sum of the first {n} natural numbers is: {num}")
else:
    print("Please enter a positive number greater than zero.")