s=3
for i in range(s,0,-1):
    for j in range(1,abs(i)+1):
        print(end=' ')
    for k in range(s,abs(i)+1):
        print("*",end=' ')
    print()
