s1=input("enter the string")
s2=input("enter the string")
if(s1 in s2):
    s3=s2[0:4]+"restore"
    print("the third string is",s3)
else:
    print("s1 is not in s2")
