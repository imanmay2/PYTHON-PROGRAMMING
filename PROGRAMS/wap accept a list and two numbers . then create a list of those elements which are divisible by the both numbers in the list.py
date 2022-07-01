li=eval(input("enter the list you want"))
l2=[]
m=int(input("enter the number"))
n=int(input("enter the second number"))
for i in li:
    if(i%m==0 and i%n==0):
        l2.append(i)
print("the final ist is")
print(l2)
