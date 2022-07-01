def count():
    ct=0
    with open(input("Enter the size of the file which you wanna count the size: ")) as gf:
        for i in gf.read():
            if(i!=" "):
                ct+=1
    return ct
print("Size of the file is: ",count(),"Bytes")