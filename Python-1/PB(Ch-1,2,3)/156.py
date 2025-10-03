n=int(input("Enter the number : "))
order=len(str(n))
sum=0

for i in str(n):
    sum+=int(i)**order

if sum==n:
    print("This number is the armstrong")
else:
    print("This number is the not armstrong")