n=int(input("enter the range of the program"))
x=0
print("the diarsium numbr are")
for i in range(1,n+1):
    x=x+1
    p=x
    q=x
    s=0
    c=0
    while(p!=0):
        p=p//10
        c=c+1
    while(q!=0):
        r=q%10
        s=s+r**c
        c=c-1
        q=q//10
    if(x==s):
        print(x)
   
        
        
    
