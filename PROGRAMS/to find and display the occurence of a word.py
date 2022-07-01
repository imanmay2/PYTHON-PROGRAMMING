#write a method to read lines from india.txt and find and display of the word.
with open("india.txt","r") as f:
    ct=0
    for i in f.read().split():
        if(i=="India"):
            ct+=1
    print("Count of the word is",ct)
