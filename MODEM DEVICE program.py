str1=input("enter the sentence you want").upper()
li=str1.split()
ct=0
for i in range(0,len(li)-1):
    for j in range(0,len(li[i])-1):
        g=li[i][j]+li[i][j+1]
        for k in range(i+1,len(li)):
            if(g in li[k]):
                ct+=1
print("number of such words present in the sentence is as follows",ct)
