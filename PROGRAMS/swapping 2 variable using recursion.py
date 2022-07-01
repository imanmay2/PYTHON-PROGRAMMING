def swap(a,b):
    global i
    i=i+1
    if i==1:
        a=a+b
        swap(a,b)
    elif i==2:
        b=a-b
        swap(a,b)
    elif i==3:
        a=a-b
        swap(a,b)
    elif(i==4):
        print(a,b)
global i
i=0
swap(int(input("ENTER THE NUMBER 1: ")),int(input("ENTER THE NUMBER 2: ")))
