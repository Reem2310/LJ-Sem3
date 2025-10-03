n=int(input("Enter the value: "))
if n<=1:
    print("The number is not prime")
else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print("The number is nor prime")
        else:
            print("The number is prime")