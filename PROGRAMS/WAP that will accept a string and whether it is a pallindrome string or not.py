s=input("enter the string you want")
s1=''
length=len(s)-1
while(length>=0):
    s1=s1+s[length]
    length=length-1
if(s==s1):
    print(s,"is pallindrome string")
else:
    print(s,"is not a pallinndrome string")
