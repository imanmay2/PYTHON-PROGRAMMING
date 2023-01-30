#1.Store userInp data other than  in a list and array.
ans="y"
t=tuple()
while ans=='y':
    n=eval(input("Enter the element you want to store: "))
    t=t+(n,)
    ans=input("Want to continue: y/n??")
print("DATA's ARE AS FOLLOWS: ")
print(t)


#2. WAP to convert infix to postfix and reverse of it.
#3. WAP to check precedence order of operators. Eg. Input => * and + … Output => * is in higher preceedance.
#   Eg: Input => * and / Out[ut => Same preceedance …
#4. WAP to display output in tabular format
#   (as we see in MySQL output of select command) for inputs by user.
