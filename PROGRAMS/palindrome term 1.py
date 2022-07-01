#palindrome number or not...
n=int(input("enter the number"))
a=n
rev=0
while(a!=0):
    r=a%10
    rev=(rev*10)+r
    a=a//10
if(rev==n):
    print("palindrome number")
else:
    print("not a palindrome number")
