def second(li):
    maxi=max(li)
    li.remove(maxi)
    sec_maxi=max(li)
    return (sec_maxi)
li=eval(input("enter the list you want to enter"))
x=second(li)
print("the second biggest number is",x)
