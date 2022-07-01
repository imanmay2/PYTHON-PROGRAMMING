mini=10
maxi=0
while(1):
    n=int(input("enter the number"))
    if(n==0):
        break
    elif(n<mini):
        print(min(mini,n))
        mini=n
    else:
        print(max(maxi,n))
        maxi=n
print("maximum number is",maxi)
print("minimum number entered is",mini)
