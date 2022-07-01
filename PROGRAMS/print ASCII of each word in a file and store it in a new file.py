# print the ASCII value of each word and store them in a new file.
with open("copy.txt") as f:
    data=f.read()
    with open("ASCII.txt","w") as f1:
        for i in data:
            f1.write(f"ASCCI value of{i} is {ord(i)}\n")
