#to print the file name,mode no. of words,no. of space.
with open("copy.txt") as f:
    data=f.read().split()
print("The no. of words in the file",f.name,"in mode",f.mode,"is",len(data))
    
    
