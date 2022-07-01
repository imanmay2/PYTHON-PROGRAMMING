li=eval(input("enter"))
print(li)
s=0
for i in li:
    if(i%2!=0):
        s=s+i
print("the sum of the odd numbers in the list",s)
