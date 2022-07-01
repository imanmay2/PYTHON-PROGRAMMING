n=int(input("enter the range of the pattern............"))
a=1
for i in range(1,n+1):
    for k in range(1,i+1):
        print(a,end=' ')
        if(a==1):
            a=a-1
        else:
            a=a+1
    if(i%2==1):
        a=0
    else:
        a=1
    print()
