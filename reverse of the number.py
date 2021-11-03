def rev():
    res=0
    a=n
    while(n!=0):
        r=n%10
        res=res*10+r
        n//=10
    if(a==res):
        print("plindrome")
    else:
        print("not palindrome")
n=int(input("enter the number"))
rev()



