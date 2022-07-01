# wap to read out the roll number and marks of 4 students and create a dictionary to print this.
rno=[]
mks=[]
for i in range(4):
    r,m=eval(input("enter the roll number, and marks"))
    rno.append(r)
    mks.append(m)
d={rno[0]:mks[0],rno[1]:mks[1],rno[2]:mks[2],rno[3]:mks[3]}
print("Created dictionary",d)

#wap to check if roll no. 2 has scored more than 75 marks or not.
if(d[2]>75):
    print("Roll no. 2 has secured more than 75 ")
else:
    print("Roll no. 2 has scored less than 75 ")


#wap to check if anyone has secured marks as 89.9
if(89.9 in d.values()):
    print("yes someone has secured marks as 89.9")
else:
    print("no one has secured marks as 89.9")


#wap to add students roll no. and marks and print the modified dictionary after adding

print("Want to add more students")
ans=input("enter yes/no").lower()
if(ans=="yes"):
    n1=int(input("how many students"))
    for j in range(n1):
        r1,m1=eval(input("enter the roll number, and marks"))
        d[r1]=m1
    print("Modified dictionary is",d)
        
