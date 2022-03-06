# swapping the keys and values of the dictionaries
d={"v1":"k1","v2":"k2"}
d1={}
for i in d:
    d1[d[i]]=i
print("The dictionary after swapping is")
print(d1)
