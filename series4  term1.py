x=int(input("enter the number you want to enter"))
n=int(input("enter the range of the series"))
s=0
for i in range(0,n):
    s=s+(x**i)
print("the sum of the series is",s)
    
