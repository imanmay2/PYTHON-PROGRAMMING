n=int(input("enter the number"))
if(n>0):
    print("the converted number is",n-(n*2))
elif(n<0):
    print("the converted number is",abs(n))
elif(n==0):
    print(n,"is neither negative nor a positive number")
