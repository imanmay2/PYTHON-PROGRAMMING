# auto biographical number
def auto_biographical(n):
    sum=0
    ct=0
    while(n!=0):
        r=n%10
        ct+=1
        sum+=r
        n=n//10
    if(sum==ct):
        print("Auto-Biographical number") 
    else:
        print("Not an Auto-Biographical number") 
n=int(input("Enter the number"))
auto_biographical(n)

