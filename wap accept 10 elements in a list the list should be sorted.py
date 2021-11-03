#wap accept 10 elements in a list the list should be sorted
#display the differenece of each element of the two new list of same index.
li=eval(input("enter the list"))
li1=sorted(li)
li2=sorted(li,reverse=True)
for i in range(0,10):
    d=li1[i]-li2[i]
    print(d)
