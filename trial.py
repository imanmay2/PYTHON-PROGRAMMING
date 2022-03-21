userInp = input("Enter sentence: ").strip().upper().split(" ")
for i in range(len(userInp)):
    for j in range(len(userInp[i])-1):
        if chr(ord(userInp[i][j])+1) == userInp[i][j+1]:
            print(userInp[i], end=" ")
            break
