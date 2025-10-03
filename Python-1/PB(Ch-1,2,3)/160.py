n=int(input("Enter the value : "))
for i in range(1,n+1):
    for r in range(1,i+1):
        print(" ",end=" ")
    for b in range(i,n+1):
        print("*",end=" ")
    print()