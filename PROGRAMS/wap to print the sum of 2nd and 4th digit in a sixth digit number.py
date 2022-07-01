#wap to print the sum of 2nd and 4th digit in a sixth digit number
n=int(input("enter a number"))
print("The sum of the 2nd and 4th digit is")
s=0
ct=6
while(n!=0):
    r=n%10
    if(ct==4 or ct==2):
        s+=r
    n=n//10
    ct-=1
print(s)
