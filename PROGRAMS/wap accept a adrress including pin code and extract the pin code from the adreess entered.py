str1=input("enter your address with pincode")
d="123456789"
s=" "
for i in str1:
    if(i in d):
        s=s+i
print("the extraction of the pin code is",s)
        
