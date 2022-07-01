n=int(input("enter the range of the program"))
a=65
n=n*2
for i in range(1,n+1,2):
    for j in range(1,(n-i)+1):
        print(end=' ')
    for k in range(1,i+1):
        print(chr(a),end=' ')
    a=a+2
    print()
