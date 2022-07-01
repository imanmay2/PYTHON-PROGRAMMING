li=eval(input("enter the list you want to enter"))
maxi=max(li)
ln=len(li)
indx=li.index(maxi)
if(indx<(ln/2)):
   print(maxi,"the maximum element is present in the first half")
elif(indx>(ln/2)):
    print(maxi,"the maximum  umber is present in the second half")
elif(indx==(ln/2)):
   print(maxi,"the maximum element is present in the equal of the list")
