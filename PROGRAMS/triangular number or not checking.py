n=int(input("enter the number"))
s=0
for i in range(1,n+1):
    s=s+i
    if(s>=n):
        break
if(s==n):
    print(n," is triangular number")
else:
    print(n," is not triangular number")
