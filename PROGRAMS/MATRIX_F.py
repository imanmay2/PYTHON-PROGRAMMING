
# for 1st row......
def row_1(li):
    r=li.pop(0)
    li.append(r)
    return li

# for 2nd row
def row_2(i):
    r1=i.pop(0)
    r2=i.pop(0)
    i.extend([r1,r2])
    return i

# for 3rd row
def row_3(j):
    r3=j.pop()
    j.insert(0,r3)
    return j


