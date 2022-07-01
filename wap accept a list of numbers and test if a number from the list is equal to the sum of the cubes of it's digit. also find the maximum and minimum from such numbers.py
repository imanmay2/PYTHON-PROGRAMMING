li=eval(input("enter the list"))
print(li)
L=[]
for i in li:
    n=i
    c=0
    while n:
        r=n%10
        c=c+(r**3)
        n=n//10
    if(c==i):
        L.append(i)
print("The maximum sum of the cube of it's digit is",max(L))
print("The minimum sum of the cube of it's digit is",min(L))
        
    
