def start():
    str_1=''
    with open(input("Enter any file name to open that file: ")) as f:
        for i in f.readlines():
            if(i[0]=="a" or i[0]=="A"):
                str_1=str_1+i
        return (str_1)
print(start())