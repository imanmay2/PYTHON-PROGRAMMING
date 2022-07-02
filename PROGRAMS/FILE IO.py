# Write a function that reads a file and display the words separated with #
def hass():
    file=input("Enter the file name")
    with open(file) as f:
        li=f.read().split()
        for i in li:
            if(i!=li[len(li)-1]):
                print(i,end='#')
            else:
                print(i)
hass()        


# copy text of one file to another and repeated space should be replaced by the single one  using def fucntions.
def hello():
    F=input("Enter the file name to copy from: ")
    f=input("Enter the file name to be pasted simultaneously: ")
    with open(F) as k:
        li=k.read().split()
        with open(f,"w") as K:
            for  i in li:
                K.write(i+" ")

hello()


# write a function named AMCount() that counts the occurence of A and M (including a and m) and display it.
def AMCount():
    f1=input("ENter any random file name you want")
    with open(f1,"w") as kh:
        str2=input("Enter the string you wanna enter")
        kh.write(str2)
    ct_m=ct_a=0
    with open(f1) as r:
        for i in r.read():
            if(i=="A" or i=="a"):
                ct_a+=1
            elif(i=="M" or i=="m"):
                ct_m+=1
        print("A or a: ",ct_a)
        print("M or m: ",ct_m)
AMCount()

# write a method/function DISPLAYWORDS() to read lines from any text file and display the words which are less  than 4
def DISPLAYWORDS():
    kf=input("ENter the file name which you wanna count the words: ")
    with open(kf,"r") as kgf:
        li=kgf.read().split()
        ct=0
        str3=" "
        for i in li:
            if(len(i)<4):
                str3+=i+" "
        return str3 
print(DISPLAYWORDS())



# write a function/method where to display the lines starting with A.
def start():
    str_1=''
    with open(input("Enter any file name to open that file: ")) as f:
        for i in f.readlines():
            if(i[0]=="a" or i[0]=="A"):
                str_1=str_1+i
        return (str_1)
print(start())


#create a function/method named count which will count the size of the file and display it's size in bytes.
def count():
    ct=0
    with open(input("Enter the size of the file which you wanna count the size: ")) as gf:
        for i in gf.read():
            if(i!=" "):
                ct+=1
    return ct
print("Size of the file is: ",count(),"Bytes")



# create a file with some name separated by newline characters with out using write() function.
with open("trialio.txt",'w') as jk:
    li=[]
    for i in range(input("enter the number of names you wanna enter: ")):
        name=input("enter the name you want: ")
        li.append(name)
    jk.writelines(li)

#write a method/function that will take marks, name, roll from the user and append in the text file.
def append():
    with open(input("ENTER ANY FILE NAME: "),"w") as fj:
        for i in range(int(input("ENTER HOW MANY INPUTS"))):
            name=input("enter the name of the student: ")
            roll=int(input("ENTER THE ROLL NUMBER: "))
            marks=float(input("ENTER THE MARKS OF THE STUDENT: "))
            rec=name+roll+marks+"\n"
            fj.write(rec)
append()