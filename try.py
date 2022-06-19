with open("dollar.txt") as o:
    ct=0
    for i in o.read():
        if(i!=' ' and i!="$"):
            ct+=1
        elif(i=="$"):
            break
print("NUMBER OF CHARACTERS PRESENT IN THE FILE UPTO $ CHARACTERS IS AS FOLLOWS: ",ct)
