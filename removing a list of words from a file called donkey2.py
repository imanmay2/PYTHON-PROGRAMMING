line=input("enter a line").lower()
words=["kaddu","mota","donkey","monkey"]
with open("donkey2.txt","w") as f:
    f.write(line)
t=open("donkey2.txt")
t1=t.read()
for word in words:
    if(word in t1):
        t1=t1.replace(word,"########")
t.close()
f1=open("donkey2.txt","w")
f1.write(t1)
f1.close()
