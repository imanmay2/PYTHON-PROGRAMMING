from MATRIX_F import *
n=[1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2,3,4,1,2]
l=len(n)
li1=list()
l=list()
ct=0
g=(len(n)//4)*4
for i in range(g):
    ct+=1
    l.append(n[i])
    if(ct==4):
        li1.append(l)
        ct=0
        l=[]

print(li1)  
#for i in range(4):
 #   if(i==0):
  #      li[0]=row_1(li[0])
   # elif(i==1):
    #    li[1]=row_2(li[1])
    #elif(i==2):
     #   li[2]=row_3(li[2])

