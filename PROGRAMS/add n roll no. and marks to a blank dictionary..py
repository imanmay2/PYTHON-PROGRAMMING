# add n roll no. and marks to a blank dictionary.
d={}
n=int(input("How many roll numbers??????"))
for i in range(n):
    r=int(input("Enter your roll number"))
    m=float(input("Enter your marks"))
    d[r]=m
print("Dictionary created is as follows")
print(d)
d[5]=88.9
print("Now dictionary is as follows")
print(d)
del d[5]
print("Dictionary now is")
print(d)
