#Program to sort name,age and height tuples in ascending order where name in str and age and height are in int
#The sorting criteria is in : name>age>height.
#If users gives in the output:
#Tom,19,80
#John,20,90
#Jony,17,91
#Jony,17,93
#Json,21,85
#Then the output will be like :[(John,20,90),(Jony,17,91),(Jony,17,93),(Json,21,85,(Tom,19,80))]
li=[]
R=int(input("Enter the range"))
for i in range(1,R+1):
    t=tuple()
    n=input("Enter the name")
    sp=n.split(",")
    for j in sp:
        t=t+(j,)
    li.append(t)
for j in range(0,R-1):
    for i in range(0,R-1):
        if(li[i][0]>li[i+1][0]):
            s=li[i]
            li[i]=li[i+1]
            li[i+1]=s
for i in range(0,R-1):
    if(li[i][0]==li[i+1][0] and li[i][1]>li[i+1][1]):
        s1=li[i]
        li[i]=li[i+1]
        li[i+1]=s1
for i in range(0,R-1):
    if(li[i][1]==li[i+1][1] and li[i][2]>li[i+1][2]):
        s2=li[i]
        li[i]=li[i+1]
        li[i+1]=s2
print("................THE LIST AFTER SORTING IN THE PROPER ASCENDING WAY IS...............")
print(li)



