def string(name,gen):
    if(gen=="M"):
        return("Mr.",name)
    elif(gen=="F"):
        return("Mrs",name)
    else:
        print("invalid character")
name=input("enter your name")
gen=input("enter your gender i.e male for M or female for F")
print("your updated name is",string(name,gen))
