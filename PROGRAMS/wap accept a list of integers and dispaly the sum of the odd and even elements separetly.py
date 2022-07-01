li=eval(input("enter the list"))
s=sum(li)
print("the sum of the integers are",s)
s1=s2=0
for i in li:
    if(i%2==0):
        s1=s1+i
    else:
        s2=s2+i
print("the sum of the even elements are",s1)
print("the sum of the odd elements are",s2)
