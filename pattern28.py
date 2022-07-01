n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j==3 or i==3):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()
