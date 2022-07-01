# wap to create a dictionary containing names of compeitition winner students as keys and no. of wins as their values
n=int(input("how many students????"))
M={}
for i in range(n):
    key=input("enter the name")
    value=int(input("enter the no. of wins till now"))
    M[key]=value
print(".....THE CREATED DICTIONARY IS.......")
print(M)
