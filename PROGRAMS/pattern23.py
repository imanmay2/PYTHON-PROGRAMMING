n=int(input("enter the range of the pattern....."))
for i in range(1,n+1):
    a=1
    b=2
    for j in range(1,i+1):
        if(i%2!=0):
            print(a,end=' ')
            a=a+2
        else:
            print(b,end=' ')
            b=b+2
    print()
