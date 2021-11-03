n=int(input("enter the range of the pattern"))
print("THE PATTERN is ...................")
for i in range(1,n+1):
    print(" "*n,"*"*i," "*n)
    n=n-1
