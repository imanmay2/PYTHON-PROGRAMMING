s=input("ENTER THE STRING: ")
for i in s:
    if(i.islower()):
        with open("lower.txt","a") as l:
            l.write(i)
    elif(i.isupper()):
        with open("upper.txt","a") as w:
            w.write(i)
    else:
        with open("others.txt","a") as h:
            h.write(i)
    