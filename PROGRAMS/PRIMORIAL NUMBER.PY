def prime(n):
    ct=0
    for i in range(1,n+1):
        if(n%i==0):
            ct+=1
    if(ct==2):
        return True
def fact(n):
    f=1
    for j in range(1,n+1):
        if(prime(j)==True):
            f=f*j
    return f 
num=int(input("Enter the number : "))
if(prime(num)!=True):
    print("..........NOT A PRIMORIAL NUMBER.........")
else:
    print("PRIMORIAL NUMBERS FACTOR'S IS AS FOLLOWS: ",fact(num))
