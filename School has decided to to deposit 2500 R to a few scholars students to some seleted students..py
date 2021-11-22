# School has decided to to deposit 2500 R to a few scholars students to some seleted students.
# Wap to input students roll number and create the dictionary for the same.
l=[]
n=int(input("How many students????"))
for i in range(n):
    r=int(input("enter the roll numbers"))
    l.append(r)
print("Created dictionary is")
s=dict.fromkeys(l,2500)
print(s)
    
