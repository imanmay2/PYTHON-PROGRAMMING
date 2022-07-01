myl=[2,4,6]
print("existing list is",myl)
n=eval(input("enter a number or a list"))
if type(n)==type([]):
    myl.extend(n)
elif(type(n)==type(1)):
    myl.append(n)
else:
    print("enter any number you want")
print("Apennded list is",myl)
