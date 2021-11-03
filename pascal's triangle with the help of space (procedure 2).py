n=int(input("enter the size of the pascal's triangle"))
for i in range(1,n+1):
    for j in range(n-1,i-1,-1):
        print(" ",end=' ')
    for k in range(i-1,-(i-1)-1,-1):
        print(i-(k*(-1)),end=' ')
    print()
    
