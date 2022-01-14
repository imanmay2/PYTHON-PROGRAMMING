n1=int(input("Enter the number you want"))
n2=int(input("Enter the second number you want"))
m=max(n1,n2)
i=2
flag=0
pro=0
while(i<=m):
    if(n2%i==0 and n1%i==0):
        li_x=list(str(n1%i))
        li_y=list(str(n2%i))
    
        if(li_x in li_y and li_y in li_x):
            flag=1
            x=n1%i
            y=n2%i
            n1=x
            n2=y
            i=1
            i=i+1
        else:
            x=n1%i
            y=n2%i
            n1=x
            n2=y
            i=1
            i=i+1
    else:
        pri_n1=0
        cn1=0
        for d in range(1,n1+1):
            if(n1%d==0):
                cn1=cn1+1
        if(cn1==2):
            pri_n1=1
        pri_n2=0
        cn2=0
        for j in range(1,n2+1):
            if(n2%j==0):
                cn2=cn2+1
        if(cn2==2):
            pri_n2=1
        if(pri_n1==1 or pri_n2==1):
            if(n1+1==n2 or n2+1==n1):
                pro=1
                break
        else:
            i=i+1
if(flag==1 and pro==1):
    print("Terrace Number")
else:
    print("Not a Terrace number")
        
        
    
