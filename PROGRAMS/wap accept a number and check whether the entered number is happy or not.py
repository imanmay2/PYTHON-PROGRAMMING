n=int(input("enter the number"))
p=0
if(n>0 and n<10):
    print("not happy number")
else:
    while(1):
        s=0
        while(n!=0):
            r=n%10
            s=s+(r*r)
            n=n//10
        if(s<10):
            p=s
            break
        else:
            n=s
    if(p==1):
        print("happy number")
    else:
        print("sad number")

            
