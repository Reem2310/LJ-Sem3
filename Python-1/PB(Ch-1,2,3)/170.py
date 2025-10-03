rows = 4
for i in range(1, rows + 1):
    for j in range(rows-i):
        print("",end=" ")
    if i%2!=0:
        symbol="*"
    else:
        symbol="#"
    
    for k in range(i):
        print(symbol,end=" ")
    
    print()
