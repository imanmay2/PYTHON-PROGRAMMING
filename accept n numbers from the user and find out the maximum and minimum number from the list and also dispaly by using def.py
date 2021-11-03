def maxmin(n):
    li=[]
    for i in range(1,n+1):
        num=int(input("enter the number you want"))
        li.append(num)
    maxi=max(li)
    mini=min(li)
    print(li)
    print("the maximum number among the list is",maxi)
    print("the maximum number among the list is",mini)
n=int(input("enter the rang of the number you have to entered"))
maxmin(n)
        
        
