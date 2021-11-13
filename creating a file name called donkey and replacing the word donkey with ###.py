line=input("enter a line").lower()
with open("donkey.txt","w") as f:
    f.write(line)
t=open("donkey.txt")
t1=t.read()
if("donkey" in t1):
    t1=t1.replace("donkey","########")
t.close()
f1=open("donkey.txt","w")
f1.write(t1)
f1.close()
