r=int(input("enter the number of rows you want to print"))
for i in range(0,r):
    for k in range(r,i,-1):
        print(end=' ')
    n=1
    for j in range(0,i+1):
        if(i==2 or i==1):
            break
        else:
            
            print(n,end=' ')
            n=n*(i-j)//(j+1)
    print()
