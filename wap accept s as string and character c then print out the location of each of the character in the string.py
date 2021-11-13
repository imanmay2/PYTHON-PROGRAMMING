s=input("enter the string")
c=input("enter the character")
l=len(s)
ct=0
print("The position of",c,"present in",s,"are",end=' ')
for i in range(l):
    if(c==s[i]):
        print(i+1,end=' ')
