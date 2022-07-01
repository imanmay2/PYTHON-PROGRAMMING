#1. write a function stats() that accepts a filename and reports the file's longest line.
def stats():
    filename=input("Enter the file name")
    with open(filename.txt,"r") as f:
        long=""
        k=f.readline()
        for i in k:
            if(len(i)>len(long)):
                long=i
        print("LOngest line is",long)