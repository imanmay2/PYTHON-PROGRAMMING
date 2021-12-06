# wap to print the sum of the series of cos(x) where the cos x is in the input in degree.
#   cos(x) = 1 - (x**2)/2! + (x**4)/4! - (x**6)/6!......(x**n)/n!
# print the sum of the cos(x)
n=int(input("enter the range of the program"))
r=2
s=0
f=1
p=float(input("Enter the value in degree"))
x=(p*3.14)/180      # converting from degree into radians
for i in range(1,n+1):
    f=f*r
    if(i%2==0):
        s+=(x**r)/f
    else:
        s-=(x**r)/f
print("The sum of the cos",p,"is",s+1)
    
    
