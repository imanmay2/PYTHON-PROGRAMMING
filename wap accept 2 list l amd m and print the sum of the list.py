L=eval(input("enter the list you wan to enter"))
M=eval(input("enter the list you want"))
li=[]
if(len(L)==len(M)):
    for i in range(0,len(M)):
        s=L[i]+M[i]
        li.append(s)
    print("the list is",li)
else:
    print("the length of the two lists are not equal")
        
    
