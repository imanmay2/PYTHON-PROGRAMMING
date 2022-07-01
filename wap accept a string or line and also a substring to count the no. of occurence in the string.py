str1=input("enter the string you want to enter")
sub=input("enter the sub-string")
l=str1.split()
ct=0
for i in l:
    if(sub in i):
        ct=ct+1
print("the no. of occurence is",ct)
