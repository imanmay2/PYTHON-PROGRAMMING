# Create a binary file with the name and roll no,search for a given roll number and display the name, if not found display appropiate message.
import pickle
with open("abab.dat","wb") as f1:
    d=dict()
    for i in range(int(input("Enter the range: "))):
        d["Roll"]=int(input("Enter the Roll number of the student: "))
        d["Name"]=input("Enter the name of the student: ")
        pickle.dump(d,f1)
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
        
            
