def pascal_triangle(number):
    for i in range(0,number):
        for k in range(number,i,-1):
            print(end=' ')
        num=1
        for j in range(0,i+1):
            print(num,end=' ')
            num=num*(i-j)//(j+1)
        print()



def two_digit_special(number):
    s=0
    n=number
    p=1
    a=n
    if(n>9 and n<100):
        while(n!=0):
            r=n%10
            p=p*r
            s=s+r
            n=n//10
        if(s+p==a):
            print(a,"is a 2-digit special number")
        else:
            print(a,"is not a 2-digit special number")
    else:
        print(a,"is not a 2-digit special number")


def krishnamurti(number):
    s=0
    n=number
    a=n
    while(n!=0):
        f=1
        r=n%10
        for i in range(1,r+1):
            f=f*i
        s=s+f
        n=n//10
    if(s==a):
        print(a,"is a KRISHNAMURTI NUMBER")
    else:
        print(a,"is not a KRISHNAMURTI NUMBER")


def pronic(number):
    # pronic number is also called heteromecic number
    flag=0
    n=number
    for i in range(0,n):
        if(i*(i+1)==n):
            flag=1
            break
    if(flag==1):
        print(n,"is a PRONIC/HETEROMECIC NUMBER")
    else:
        print(n,"is not a PRONIC/HETEROMECIC NUMBER")


def darsium(number):
    s=0
    n=number
    c=0
    p=n
    x=n
    while(p!=0):
        p=p//10
        c+=1
    while(n!=0):
        r=n%10
        s=s+(r**c)
        c=c-1
        n=n//10
    if(s==x):
        print("DARSIUM NUMBER")
    else:
        print("NOT A DARSIUM NUMBER")


def happy(number):
    p=0
    n=number
    if(n>0 and n<10):
        print("NOT A HAPPY NUMBER")
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
            print("HAPPY NUMBER")
        else:
            print("NOT A HAPPY NUMBER")


            
