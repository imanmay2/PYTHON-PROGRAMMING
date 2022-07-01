for i in range(1,5):
    for j in range(4,i,-1):
        print(" ",end=' ')
    for k in range(i-1,-i,-1):
        print(i-abs(k),end=' ')
    print()
