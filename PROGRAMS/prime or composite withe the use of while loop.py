n=int(input("enter the number"))
i=1
ct=0
while(i<=n):
    if(n%i==0):
        ct+=1
    i=i+1
if(ct==2):
    print(n,"is prime")
else:
    print(n,"is a composite")
