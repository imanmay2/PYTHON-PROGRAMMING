def rev(n):
    while(n!=0):
        r=n%10
        res=res*10+r
        n=n//10

rev(1234)
print("the reverse of the entered number",res)
