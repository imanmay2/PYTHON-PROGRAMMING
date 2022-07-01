#program to find the frequency of the numbers given in the list
li=[1,2,4,2,6,7,4]
d=dict()
for s in li:
    if(s in d):
        d[s]+=1
    else:
        d[s]=1
print(d)
        
