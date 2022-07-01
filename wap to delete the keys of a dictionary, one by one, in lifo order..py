# wap to delete the keys of a dictionary, one by one, in lifo order.


stu={1:"smita",2:"Munna",3:"bhai"}
length=len(stu)
while(length>=1):
    print("Element deleted is",stu.popitem())
print("All elements are delted in the lifo order")
