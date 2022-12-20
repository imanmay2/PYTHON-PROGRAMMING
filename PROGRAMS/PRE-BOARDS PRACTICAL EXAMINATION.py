#1. Read a text file and the number of uppercase/lowercase characters in the file.
with open("abab.txt","w") as f:
    f.write("Hello")
with open("abab.txt") as k:
    ct_U=0
    ct_L=0
    for i in k.read():
        if(i.isupper()):
            ct_U+=1
        elif(i.islower()):
            ct_L+=1
    print("Count of the uppercase and lowercase letters are as follows: ",ct_U,ct_L)

# Create a binary file with the name and roll no,search for a given roll number and
# display the name, if not found display appropiate message.
import pickle
with open("abab.dat","wb") as f:
    d=dict()
    for i in range(int(input("Enter the range"))):
        d["Roll"]=int(input("Enter the Roll number of the student: "))
        d["Name"]=input("Enter the name of the student: ")
        pickle.dump(d,f)
with open("abab.dat","rb") as f:
    found=0
    r=int(input("Enter the Roll number to be searched for: "))
    try:
        while True:
            g=pickle.load(f)
            if(g["Roll"]==r):
                print("Name is: ",g["Name"])
                found=1
                break
    except EOFError:
        if found==0:
            print("Oops!!can't find any name in the dictionary...")
            
