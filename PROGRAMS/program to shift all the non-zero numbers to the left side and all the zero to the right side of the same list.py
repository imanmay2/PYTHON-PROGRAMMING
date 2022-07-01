# program to shift all the non-zero numbers to the left side and all the
# zero numbers to the right side of the same list.
li=eval(input("Enter the list"))
li_0=[]
li_1=[]
for i in li:
    if(i==0):
        li_0.append(i)
    else:
        li_1.append(i)
print("The final list becomes is",li_1+li_0)
