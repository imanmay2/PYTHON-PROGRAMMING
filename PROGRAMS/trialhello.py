with open("poem.txt") as f:
    with open("poem1.txt") as g:
        str=' '
        while str:
            str=f.readline()+g.readline()
            print(str)
