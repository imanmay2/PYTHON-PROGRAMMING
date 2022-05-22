with open("poem1.txt","r") as f:
    n=int(input("ENTER HOW MAY BYTES DO YOU WANNA PRESENT IN THE SHELL????  "))
    str1=f.read(n)
    print(str1)