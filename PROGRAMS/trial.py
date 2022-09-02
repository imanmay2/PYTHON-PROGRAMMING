import pickle
with open("stud11.dat","rb") as f:
    try:
        while True:
            emp=pickle.load(f)
            print(emp)
    except EOFError:
        f.close()
