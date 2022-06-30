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