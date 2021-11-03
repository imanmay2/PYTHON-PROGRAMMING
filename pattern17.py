for i in range(1,5):
    for j in range(1,(4-i)+1):
        print(end=' ')
    for k in range(1,i+1):
        if(k%2==0):
            print("0",end=' ')
        else:
            print("1",end=' ')
    print()
