n=input("enter the numbers ")
l=list(n)
ct=0
for i in range(1,l+1):
    if(l%i==0):
        ct=ct+1
if(ct==2):
    print(l)
