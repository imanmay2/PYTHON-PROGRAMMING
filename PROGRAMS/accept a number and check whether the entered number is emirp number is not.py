n=int(input("enter the number"))
ct=0
f=0
q=0
t=n
res=0
c=0
for i in range(1,n+1):
    if(n%i==0):
        ct=ct+1
if(ct==2):
    f=1
while(t!=0):
    r=t%10
    t=t//10
    res=(res*10)+r
for j in range(1,res+1):
    if(res%j==0):
        c=c+1
if(c==2):
    q=1
if(q==1 and f==1):
    print("the number that you have entered is an emirp number")
else:
    print("the number that you have entered is not an emirp number")
