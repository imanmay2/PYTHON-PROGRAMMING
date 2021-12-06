#      .........................KEITH NUMBER...........................
# e.g.....197,19,742, 1537,etc....


x=int(input("Enter the number"))#742
n=str(x)
s=0
k=[]
for i in n:
    k.append(int(i))
    s=s+int(i)
k.append(s)

while(1):
    k.pop(0)
    s1=sum(k)
    k.append(s1)
    if(s1==x):
        f=1
        break
    elif(s1>x):
        f=2
        break
if(f==1):
    print(x,"is a keith number")
elif(f==2):
    print(x,"is not a keith number")


