li=[5,3,2,1]
for i in range(0,len(li)-1):
    for j in range(0,len(li)):
        if(li[j]>li[j+1]):
            li[j],li[j+1]=li[j+1],li[j]
print(li)
