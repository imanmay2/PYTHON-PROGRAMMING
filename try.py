s=input("ENTER THE STRING: ")
for i in s:
    if(i.islower()):
        with open("lower.txt","w") as l:
            l.write(i)
    elif(i.isupper()):
        with open("upper.txt","w") as w:
            w.write(i)
    else:
        with open("others.txt","w") as h:
            h.write(i)