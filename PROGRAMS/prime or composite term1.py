#prime number or not....
n=int(input("enter the number"))
ct=0
for i in range(1,(n//2)+1):
    if(n%i==0):
        ct+=1
if(ct==1):
    print("prime number")
else:
    print("composite number")
