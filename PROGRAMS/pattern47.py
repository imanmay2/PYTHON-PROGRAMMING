n=3
for i in range(n,-n+1,-1):
    if(i<0):
        i=i*(-1)
    for j in range(1,i+1):
        print(" ",end=' ')
    for k in range(n,-n+1,-1):
        print("*",end=' ')
    print()
