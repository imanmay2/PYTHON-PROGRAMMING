file_name=input("ENTER THE FILE_NAME: ")
with open("poem.txt","r") as y:
    str1=y.read()
with open(file_name,"w") as j:
    j.write(str1)
