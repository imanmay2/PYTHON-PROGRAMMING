def func1():
    with open("onn.txt","r") as f1:
        upp=''
        lo=''
        oth=''
        for i in f1.read():
            if(i.islower()):
                f2=open("lower.txt",'w')
                lo=lo+i
                f2.write(lo)
            elif(i.isupper()):
                f3=open("upper.txt",'w')
                upp=upp+i
                f3.write(upp)
            else:
                f4=open("others.txt","w")
                oth=oth+i
                f4.write(oth)
func1()
                
