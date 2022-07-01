
# sorting using lambda function
s={(1,2),(3,1),(4,0)}
p=sorted(s.items(),key=lambda kv:kv[1])
print(s)
