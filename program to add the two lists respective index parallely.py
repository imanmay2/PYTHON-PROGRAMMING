# L=[3,1,4]     M=[1,5,9]
# final output should come ::::     [4,6,13]
# program to add the two lists respective index parallely

L=eval(input("Enter the list"))
M=eval(input("Enter the list"))
s=[]
if (len(L)==len(M)):
    for i in range(0,len(L)):
        sum=L[i]+M[i]
        s.append(sum)
    print(s)
else:
    print("List are not of the same size")
    
    
