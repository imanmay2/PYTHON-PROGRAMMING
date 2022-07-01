line=input("enter the poem you want to enter").lower()
p=open("poem.txt","w")
p.write(line)
p.close()
f=open("poem.txt")
t=f.read()
if("twinkle" in t):
    print("Twinkle word is present in that file")
else:
    print("Twinkle word is not present in that file")
f.close()
    

