# 1.
def AMCount():
    ct=ct_m=0
    with open("PROGRAMS/poem1.txt") as f:
        for i in f.read():
            if(i=="A" or i=="a"):
                ct+=1
            elif(i=="M" or i=="m"):
                ct_m+=1
    return ct,ct_m
print("Count of A ora and M or m is: ",AMCount(),respectively)

#2. 
import pickle
def countrec():
    