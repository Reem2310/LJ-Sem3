# Write a program to find the factorial of a number provided by the user.

num=int(input("Enter the number: "))
if num>0:
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
        print(f"The {num} Number of factorial is :{factorial}")
elif num==0:
    print("The number of 0 is 1")
else:
    print("The negative number is not allowed. ")