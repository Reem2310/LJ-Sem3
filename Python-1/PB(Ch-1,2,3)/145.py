#Write a Python Program to Compute the product of the odd digits in a given number,0 if there are not any odd digits in a given number.
n=input("Enter the number : ")
product=1
odd_digit=False
for digit in n:
    di=int(digit)
    if di%2!=0:
        product*=di
        odd_digit=True
if odd_digit:
    print(f"The Output is : {product}")
else:
    print("The Output is 0.")

