# 5. wap to repeatedly accpet the product name and price of the product and if the user wants to add something he/she may also want.
ans="yes"
m={}
while(ans=="yes"):
    n=int(input("how many products"))
    for i in range(n):
        pn=input("enter the product name")
        pp=int(input("enter the price of the entered product"))
        m[pn]=pp
    print("the created dictionary is")
    print(m)
    ans=input("want to want to add more items and price").lower()
    
