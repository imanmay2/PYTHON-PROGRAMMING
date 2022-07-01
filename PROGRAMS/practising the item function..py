#  item() function.

emp={"name":"John","Salary":25000,"Age":25}
item=emp.items()
for i in item:
    print(i)




# keys() and values() method.

emp={"name":"John","Salary":25000,"Age":25}
print("Keys are as follows",emp.keys())
print("values are as follows",emp.values())





# get() function.

emp={"name":"John","Salary":25000,"Age":25}
print(emp.get("Salary"))



#  fromkeys() function.

d=dict.fromkeys((3,4,8),(89,67,56))
print(d)


# setdefault() function.

emp={1:2,2:3}
emp.setdefault(68,80)
print(emp)


# example of set default() function.
d1={}
val1=d1.setdefault(30,"r")
val2=d1.setdefault(30,"rr")
val3=d1.setdefault(40)
print(val1,val2,val3)

# pop() function.

stu={1:"smita",2:"Munna",3:"bhai"}
d=stu.pop(3,"not here")
print(d)
print(stu)

# pop item() function.

stu={1:"smita",2:"Munna",3:"bhai"}
stu.popitem()
print(stu)




























