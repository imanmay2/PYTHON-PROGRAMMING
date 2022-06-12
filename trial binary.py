import pickle
f=0
with open("stu1.dat","rb") as f3:
    try:
        while True:
            d=pickle.load(f3)
            if(d["marks"]>81.0):
                print(d)
                f=1
    except EOFError:
        if(f==0):
            print("NO RECORDS FOUND IN THE DATABASE.....")
            