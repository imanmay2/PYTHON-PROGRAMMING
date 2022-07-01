str1=input("enter the formula which icludes the parenthesis")
ct=0
for i in str1:
    if(i=="("):
        ct+=1
    elif(i==")"):
        ct-=1
if(ct==0):
    print("the formula is valid")
else:
    print("invalid formula! please enter a valid one")
    
