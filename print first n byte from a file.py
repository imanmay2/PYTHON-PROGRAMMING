#1.  read n byte and display in the python shell after reading....
with open("poem1.txt","r") as f:
    n=int(input("ENTER HOW MAnY BYTES DO YOU WANNA PRESENT IN THE SHELL????  "))
    str1=f.read(n)
    print(str1)

#2. read n bytes and then reading some more bytes from the last portion....
with open("poem1.txt","r") as f:
    n=int(input("ENTER HOW MAnY BYTES DO YOU WANNA PRESENT IN THE SHELL????  "))
    n1=int(input("ENTER HOW MAnY  MORE BYTES DO YOU WANNA PRESENT IN THE SHELL????  "))
    str1=f.read(n)
    str2=f.read(n+n1)
    print(str1)
    print(str2)

#3. Reading files entire content.
with open("poem1.txt","r") as f:
    print("FILES ENTIRE CONTENT IS AS FOLLOWS:  ")
    print(f.read())

#4. Reading first three lines of the poem1.txt....
with open("poem1.txt","r") as f:
    print(f.readline(),end=' ')
    print(f.readline(),end=' ')
    print(f.readline(),end=' ')
