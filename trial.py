li1=eval(input("ENTER THE LIST 1: "))
li2=eval(input("ENTER THE LIST 2: "))
li3=[]
if(len(li1)!=len(li2)):
    print("ERROR FOUND!!!! ENTER TWO LISTS WITH SAME LENGTH")
else:
    for i in range(len(li1)):
        s=0
        s=li1[i]+li2[i]
        li3.append(s)
    print("LIST 3 IS AS FOLLOWS",li3)