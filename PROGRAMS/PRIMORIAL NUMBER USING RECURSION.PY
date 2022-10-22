def prime(n):
    ct=0
    for i in range(1,n+1):
        if(n%i==0):
            ct+=1
    if(ct==2):
        return True
def primo(n):
    if(n==1):
        return 1
    else:
        if prime(n)==True:
            return n*primo(n-1)
        else:
            return primo(n-1)

num=int(input("Enter the number you want to enter: "))
if(prime(num)==True):
    print("PRIMORIAL OF THE NUMBER IS: ",primo(num))
else:
    print("....PRIME NUMBER NOT ENTERED....")

    


