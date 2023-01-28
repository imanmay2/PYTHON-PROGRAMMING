#1.Store userInp data other than  in a list and array.
ans="y"
t=tuple()
while ans=='y':
    n=eval(input("Enter the element you want to store: "))
    t=t+(n,)
    ans=input("Want to continue: y/n??")
print("DATA's ARE AS FOLLOWS: ")
print(t)
