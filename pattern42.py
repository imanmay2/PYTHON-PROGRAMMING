for i in range(1,10):
    for j in range(i,0,-1):
        if(j%2!=0):
            print(j,end=' ')
            if(i%2==0):
                print(i,end=' ')
    print()
