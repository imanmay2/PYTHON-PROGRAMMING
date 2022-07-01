import pickle
member=dict()
ans='y'
while ans=="y":
    with open("ex.dat","wb") as g:
        mem=int(input("ENTER THE MEMBER NO. : "))
        name=input("ENTER THE NAME OF THE MEMBER: ")
        member["MemberN0."]=mem
        member["Name"]=name
        pickle.dump(member,g)
        ans=input("DO YOU WANNA ENTER MORE ENTRIES: ??")
with open("ex.dat") as kl:
    try:
        while True:
            rec=pickle.load(kl)
            print(rec)
    except EOFError:
        kl.close()