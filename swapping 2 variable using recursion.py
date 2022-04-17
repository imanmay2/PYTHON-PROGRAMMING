def swap(a,b):
    global i
    i=i+1
    if i==1:
        a=a+b
        swap(a,b)
    if i==2:
        b=a-b
        swap(a,b)
    if i==3:
        a=a-b
        swap(a,b)
    if(i==4):
        return a,b
a=int(input("ENTER THE NUMBER 1: "))
b=int(input("ENTER THE NUMBER 2: "))
global i
i=0
print(swap(a,b))
