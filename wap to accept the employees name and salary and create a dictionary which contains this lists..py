# 1. wap to accept the employees name and salary and create a dictionary which contains this lists.
n=int(input("enter the no. of employees input in the dictionary"))
dic={}
for i in range(n):
    e=input("enter the name of the employee")
    s=int(input("enter the salary of that very employee"))
    dic[e]=s
print("the created dictiuonary is",dic)


    
    
