
with open("lines.txt") as f:
    ct=1
    for i in f.readlines():
        for j in i:
            if(j==' '):
                ct+=1
                if(ct==5):
                    print(i)