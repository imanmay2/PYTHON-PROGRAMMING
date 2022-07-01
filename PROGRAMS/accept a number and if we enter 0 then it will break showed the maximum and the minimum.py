f=0
mini=0
maxi=0
while(1):
    n=int(input("enter the number"))
    if(f==0):
        f=1
        mini=n
    if(mini>n):
        mini=n
    else:
        print(max(maxi,n))
    if(n==0):
        break
print("the maximum number is",maxi)
print("the minimum number is",mini)
