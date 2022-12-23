#                       HALF YEARLY QUESTION PAPER
#1. Write a fucntion in python that counts the number of "Me" or "My" words present in a text file "STORY.TXT".
def func1():
    with open("STORY.TXT") as f:
        ct_Me=ct_My=0
        for i in f.readlines():
            if "Me" in i:
                ct_Me+=1
            elif "My" in i:
                ct_My+=1
        print("Count of Me: ",ct_Me)
        print("Count of My: ",ct_My)


#2. Write a function AMCount() in python, which should read each character of a text file STORY.TXT, should display the occurence of alphabets 
# A and M(including small cases a and m too)
def AMCount():
    with open("STORY.TXT") as f1:
        ct_M=ct_A=0
        for i in f1.read():
            if(i=="A" or i=="a"):
                ct_A+=1
            elif(i=="M" or i=="m"):
                ct_M+=1
        print("Occurences of A: ",ct_A)
        print("Occurences of M: ",ct_M)



#3. Write a method/function DISPLAYWORDS() in python to read lines from a text file STORY.TXT and display those words which are less than 4 characters.
def DISPLAYWORDS():
    with open("STORY.TXT") as f2:
        for i in f2.readlines():
            if(len(i)<4):
                print(i)



#4. Write a function that will count the number of line start with "A" from the text file ab.txt.
def func2():
    with open("ab.txt") as f3:
        ct=0
        for i in f3.readlines():
            if(i[0]=="A"):
                ct+=1
        print("No. of lines starting with A: ",ct)

#5. Write a function that will transfer all the lines start with "A" from A.txt to B.txt
def func3():
    temp_String=""
    with open("A.txt",'r+') as f4:
        with open("B.txt","w") as f5:
            for i in f4.readlines():
                if(i[0]=="A"):
                    f5.write(i)
                else:
                    temp_String+=i
        f4.seek(0)
        f4.truncate()
        f4.write(temp_String)     

# 6. A binary file "Book.dat" has structure [BookNo,Book_Name,Author,Price]
# i) Write a user defined function Create file() to input data for n records and add to Book.dat
# ii) Write a function CountRec(Author) in python which accepts the Author name as parameter and count the number of books by the 
#     given Author are stored in the binary file "Book.dat".
#solution of i)
import pickle
def func4():
    with open("Book.dat","wb") as f6:
        d=dict()
        for i in range(int(input("Enter the range: "))):
            d["BookNo"]=int(input("Enter the book no. : "))
            d["Book_Name"]=input("Enter the name of the book")
            d["Author"]=input("Enter the author name: ")
            d["Price"]=float(input("Enter the price of the book: "))
            pickle.dump(d,f6)
#Solution of ii)
def func5(Author_Name):
    with open("Book.dat","rb") as f7:
        ct_book=0
        try:
            while True:
                    dic=pickle.load(f7)
                    if(dic["Author"]==Author_Name):
                        ct_book+=1
        except EOFError:
            return ct_book

#7. Elements of a list L is 1,2,3. write a function transfer() that will transfer the element of the L in a 2d list 3 by 3.
# in such a way that the resultant 2D list will be like
#   1 2 3
#   1 2 0
#   1 0 0
def transfer():
    L=[1,2,3]
    li=[L,L,L]
    for i in range(len(li)):
        for j in range(len(li)):
            if((i==1 and j==2) or (i==2 and j==1) or (i==2 and j==2)):
                li[i][j]=0
            print(li[i][j],end=' ')
        print()


#8. Write a function that will display the first and second diagonal of the 2d list 3 by 3 by a function .Function will accept the lost as parameter
def func6(li):
    l1=list()
    l2=list()
    for i in range(len(li)):
        for j in range(len(li)):
            if((i==0 and j==0) or (i==1 and j==1) or (i==2 and j==2)):
                l1.append(li[i][j])
            elif((i==0 and j==2) or (i==1 and j==1) or (i==2 and j==0)):
                l2.append(li[i][j])
    print("1st diagonal is: ")
    for i in l1:
        print(i,end=' ')
    print("2nd diagonal is: ")
    for i in l2:                
        print(i,end=' ')



#9. Write a function that will transpose the element of a 2d list of 3 by 3 and display in the matrix format.

#10. Write a function that will display the sum of each column of a 2D list 3 by 3.
def func7(li):
    s=0
    for i in li:
        s+=sum(i)
    print("Sum of the each coloumn is: ",s)

#11. Amit has a list conataining 10 integers. You need to help him create a program with separate user defined functions 
#    to perform the following operations based on this list
#      i) Traverse the content of the list and push the even numbers into a stack.
#      ii) Pop and display the content of the stack.
def push(stk,item):
    if(len(stk==10)):
        print("OVERFLOW")
    elif(item%2==0):
        stk.append(item)
    else:
        print("NOT AN EVEN NUMBER....")
def pop(stk):
    if(stk==[]):
        print("STACK IS EMPTY")
    else:
        print("The poped element from the stack is: ",stk.pop())
def display(stk):
    if stk==[]:
        print("STACK IS EMPTY")
    else:
        print("STACK IS AS FOLLOWS: ")
        for i in range(len(stk)-1,-1,-1):
            print(stk[i])
def execute():
    print("STACKS OPERATION!!!!")
    print("1. PUSH")
    print("2. POP")
    print("3. DISPLAY")
    ch=int(input("Enter your choice: "))
    if(ch==1):
        item=int(input("Enter the item: "))
        push(stk,item)
    elif(ch==2):
        pop(stk)
    elif(ch==3):
        display(stk)
    else:
        break
execute()
#12. Write a function in python POP(Arr), where Arr is a stack implemented by a list of numbers. 
#    The function returns the content of the stack.
# solution is same as the above program....


#13. Write a function to read a text file line by line and display each word spearated by #.
def func8():
    with open("STORY.TXT") as f8:
        for i in f8.split():
            print(i,end='#')
func8()


#14. Remove all the lines that conatin the character 'a' in a file and write it to another file another.