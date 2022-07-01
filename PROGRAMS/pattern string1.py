n=int(input("ener the range of the pattern....."))
a=97
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(a),end=' ')
    print()
