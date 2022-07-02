#Program in python to type text in a file till ~ is pressed as rightmost character

with open("stu.txt","w") as f:
    while True: 
        str2=input("enter the string: ")
        if(str2[-1]=="~"):
            f.write(str2)
            break
        else:
            f.write(str2+"\n")


