str1=input("enter the string")
s=''
d="1234567890"
f=0
for i in str1:
    if(i in d):
        s=s+i
        f=1
if(f==0):
    print("no digit in the string")
    s=0
elif(f==1):
    print("digits are present in the string")
s1=0
s=int(s)
while(s!=0):
    r=s%10
    s1=s1+r
    s=s//10
print("the sum of the digit is",s1)

