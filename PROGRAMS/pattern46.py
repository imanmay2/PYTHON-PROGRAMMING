size=3
for i in range(size,-size-1,-1):
    if(i<0):
        i=i*(-1)
    for j in range(1,i+1):
        print(" ",end=' ')
    for k in range(size,i-1,-1):
        print("*",end=' ')
    print()
