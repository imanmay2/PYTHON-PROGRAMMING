mini=0
maxi=0
f=0
num=1
while(num<=10):
    n=int(input("enter the number:"))
    num=num+1
    if(f==0):
        mini=n
        maxi=n
        f=1
    elif(n<mini):
        mini=n
    elif(n>maxi):
        maxi=n
print("The maximum and minimum number between 10 numbers is",maxi,mini)
