# ACCEPTING A LIST WHICH CONTAINS THE ELEMENTS OF HAVING NUMEROUS DATATYPES....AND STORE PARTICULAR DATATYPE OF ELEMENTS IN DIFFERENT REPECTIVE LISTS.
li=eval(input("Enter the list: "))
li_int=[]
li_float=[]
li_str=[]
for i in li:
    if(type(i)==type(1)):
        li_int.append(i)
    elif(type(i)==type(1.5)):
        li_float.append(i)
    elif(type(i)==type('s')):
        li_str.append(i)
print(li)
print(li_int)
print(li_float)
print(li_str)
