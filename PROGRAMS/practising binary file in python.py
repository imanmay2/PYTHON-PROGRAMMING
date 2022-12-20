with open("sample2.txt") as f:
    li=f.readlines()
    li1=list()
    for i in li:
        li1.append(len(i))
    print(li[max(li1)])


