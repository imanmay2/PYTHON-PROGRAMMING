n=int(input("enter the range of the pattern you want to print"))
px=n
py=n
for i in range(1,n+1):
    for j in range(1,n*2):
        if(j>px and j<py):
            print(" ",end=' ')
        else:
            print("*",end=' ')
    px=px-1
    py=py+1
    print()
