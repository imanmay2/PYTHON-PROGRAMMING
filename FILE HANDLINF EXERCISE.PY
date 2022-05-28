# HELLO EVERYONE....THESE ARE FEW PROGRAMS FROM THE EXCERCISE OF FILE IO...HOPE YOU WILL ENJOY IT.
# QUESTIONS ALONG WITH THEIR SOLUTIONS ARE HERE..

#4. Write a program to count the words 'to' and 'the' from the text file named poem1.txt.
with open("poem1.txt") as f:
    t=0
    th=0
    for i in f.read().split():
        if(i=="to"):
            t=t+1
        elif(i=="the"):
            th=th+1
    print("Count of the word 'to' and 'the' is: ",t,th,"respectively.")

#5. 