li=eval(input("enter the list you want to enter"))
print("original list you have entered is",li)
maxi=max(li)
l=len(li)
indx=li.index(maxi)
print("maximum number is",maxi,"at a index of",indx,"in the original list entered by the user")
li.sort()
print("sorted list is",li)
id=li.index(maxi)
if(id<=(l/2)):
   print(maxi,"the maximum element is present in the first half")
else:
    print(maxi,"the maximum  number is present in the second half")
