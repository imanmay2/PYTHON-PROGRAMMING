n=int(input("enter the range of the program"))
c=0
ct=0
for i in range(1,n+1):
    num=int(input("enter the number"))
    if(num%2==0):
        c=c+1
        print("even number",num)
    else:
        print("odd number",num)
        ct=ct+1
print("the count of even and odd numbers are",c,ct)
        
