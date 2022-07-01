inte=int(input("enter the integer you wan to enter"))
str1=input("enter the string you wan to enter")
dig="0123456789"
d=""
f=0
for i in str1:
    if(i in dig):
        d=d+i
        f=1
if(f==0):
    d="0"
print("the extract digits are",d)
s=inte+int(d)
print("the sum of the integer input and the extraction of the string input is",s)
