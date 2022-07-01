li=eval(input("Enter the list"))
n=eval(input("Enter anything to be appended like integer or list"))
if(type(n)==type([])):
    li.extend(n)
    print(li)
elif(type(n)==type(1)):
    li.append(n)
    print(li)
else:
    print("Neither an integer nor a list")
