n=8
px=1
for i in range(1,n+1):
    for j in range(1,n):
        if(j<px or j>=n-px+1):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    if(i<=n/2):
        px=px+1
    else:
        px=px-1
    print()
