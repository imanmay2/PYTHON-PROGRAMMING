with open("trialio.txt",'w') as jk:
    li=[]
    for i in range(int(input("enter the number of names you wanna enter: "))):
        name=input("enter the name you want: ")
        li.append(name+"\n")
    jk.writelines(li)