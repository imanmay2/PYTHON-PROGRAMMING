for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(i,end=' ')
    print()
n=int(input("enter the range"))
for i in range(1,n+1):
    for j in range(1,(n-i)+1):
        print(" ",end=' ')
    for k in range(1,i+1):
        print("*",end=' ')
    print()
n=int(input("enter the range"))
for i in range(1,n+1):
    for j in range(1,(n-i)+1):
        print(" ",end=' ')
    for k in range(1,i+1):
        if(i%2==0):
            print("*",end=' ')
        else:
            print("#",end=' ')
    print()

