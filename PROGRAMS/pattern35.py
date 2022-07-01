n=int(input("enter the side"))
p=" "*(n+2)
for i in range(1,n+1):
    if(i==1 or i==n):
        print("* "*n)
    else:
        print("* "+p+"*")
