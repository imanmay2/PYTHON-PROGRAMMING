n=int(input("enter the range of the pattern"))
k=0
for i in range(1,n+1):
    k=k+1
    for j in range(1,i+1):
        if(j==i or j==n-(i+1)):
            print(k,end=' ')
        else:
            print(" ",end=' ')
    print()
