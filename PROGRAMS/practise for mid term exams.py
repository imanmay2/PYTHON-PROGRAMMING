def transfer():
    l=[1,2,3]
    l1=[1,2,3]
    l2=[1,2,3]
    li=[l,l,l]
    #li=[[1,2,3],[1,2,3],[1,2,3]]
    for i in range(len(li)):
        for j in range(len(li)):
            if((i==1 and j==2) or (i==2 and j==1) or (i==2 and j==2)):
                li[i][j]=0
    for i in li:
        print(i)
transfer()

#[1,2,3]
#[1,2,3]
#[1,2,3]