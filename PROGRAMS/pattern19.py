n=int(input("enter the range of the pattern.........."))
for i in range(n,0,-1):
    for k in range(1,(n-i)+1):
        print(end=' ')
    for j in  range(1,i+1):
        print("*",end=' ')
    print()
