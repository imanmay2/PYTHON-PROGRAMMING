height=5
space=height-1
x=1
for i in range(0,height):
    for j in range(space,i-1,-1):
        print(" ",end=' ')
    for k in range(0,i+1):
        print("*",end=' ')
    for n in range((height+height-2),x-1,-1):
        print(" ",end=' ')
    for k in range(0,i+1):
        print("*",end=' ')
    x=x+2
    print()
