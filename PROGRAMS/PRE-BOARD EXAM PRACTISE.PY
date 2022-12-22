#                       HALF YEARLY QUESTION PAPER
#1. Write a fucntion in python that counts the number of "Me" or "My" words present in a text file "STORY.TXT".
def func1():
    with open("STORY.TXT") as f:
        ct_Me=ct_My=0
        for i in f.readlines():
            if "Me" in i:
                ct_Me+=1
            elif "My" in i:
                ct_My+=1
        print("Count of Me: ",ct_Me)
        print("Count of My: ",ct_My)
func1()

#2. Write a function AMCount() in python, which should read each character of a text file STORY.TXT, should display the occurence of alphabets 
# A and M(including small cases a and m too)
def AMCount():
    with open("STORY.TXT") as f1:
        ct_M=ct_A=0
        for i in f1.read():
            if(i=="A" or i=="a"):
                ct_A+=1
            elif(i=="M" or i=="m"):
                ct_M+=1
        print("Occurences of A: ",ct_A)
        print("Occurences of M: ",ct_M)
AMCount()


#3. Write a method/function DISPLAYWORDS() in python to read lines from a text file STORY.TXT and display those words which are less than 4 characters.
def DISPLAYWORDS():
    with open("STORY.TXT") as f2:
        for i in f2.readlines():
            if(len(i)<4):
                print(i)
DISPLAYWORDS()


#4. Write a function that will count the number of line start with "A" from the text file ab.txt.
def func2():
    with open("ab.txt") as f3:
        ct=0
        for i in f3.readlines():
            if(i[0]=="A"):
                ct+=1
        print("No. of lines starting with A: ",ct)
func2()