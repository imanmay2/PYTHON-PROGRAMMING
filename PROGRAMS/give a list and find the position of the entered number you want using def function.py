def search(l,item):
    f=0
    ct=0
    for i in l:
        ct=ct+1
        if(i==item):
            f=1
            print("position of",item, "is: ",ct)
            
    if(f==0):
        print("position of",item,"is not found in the list")
l=[]
n=int(input("enter the range you want to give in the list"))
for i in range(1,n+1):
    a=int(input("enter the number"))
    l.append(a)
print(l)
item=int(input("enter the number you want to search in the list"))
search(l,item)
              
    
        
        
