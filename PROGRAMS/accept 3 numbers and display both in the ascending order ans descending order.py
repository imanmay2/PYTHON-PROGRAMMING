print("enter the number")
a=int(input())
b=int(input())
c=int(input())
maxi=max(a,b,c)
mini=min(a,b,c)
l=(a+b+c)-maxi-mini
print("the numbers in ascending order is",mini,l,maxi)
print("the numbers in descending order is",maxi,l,mini)
