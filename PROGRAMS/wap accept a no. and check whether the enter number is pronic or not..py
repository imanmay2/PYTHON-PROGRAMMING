#wap accept a no. and check whether the enter number is pronic or not.
f=0
n=int(input("enter the number"))
for i in range(1,(n//2)+1):
    if(i*(i+1)==n):
        f=1
        break
if(f==0):
    print(" not pronic no.")
else:
    print("pronic one")
