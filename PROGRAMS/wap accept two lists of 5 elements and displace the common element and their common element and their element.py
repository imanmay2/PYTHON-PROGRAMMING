L1=eval(input("enter the list"))
L2=eval(input("enter the second list"))
print("the common elements :")
for i in L1:
    if(i in L2):
        print(i,end=' ')
