#10. Write a program that will input n characters from the keyboard and if the letter entered is lower , then it will get stored in the lower.txt file.similarly for others and uppercase too.
with open("poem1.txt") as f:
    for i in f.read():
        if(i.isupper()):
            with open("upper.txt","w") as f1:
                f1.write(i,end=' ')
        elif(i.islower()):
            with open("lower.txt","w") as f2:
                f2.write(i,end=' ')
        else:
            with open("others.txt","w") as f3:
                f3.write(i,end=' ')