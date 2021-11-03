def pascal_triangle(n):
    myList = []
    trow = [1]
    y = [0]
    for x in range(max(n,0)):
        myList.append(trow)
        trow=[l+r for l,r in zip(trow+y, y+trow)]

    for item in myList:
        print(item)

pascal_triangle(5)
