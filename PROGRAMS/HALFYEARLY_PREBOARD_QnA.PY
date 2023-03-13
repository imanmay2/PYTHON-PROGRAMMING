#                                                       HALF-YEARLY QUESTION PAPER
# 1. A binary file ''Book.dat" has structure [BookNo,Book_Name,Author,Price].
# i) Write a user defined function CreateFile() to input for a recorde and add to Book.dat
import pickle
def CreateFile():
    with open("Book.dat","wb") as f:
        d={}
        n=int(input("Enter how many inputs : "))
        for i in range(n):
            d['BookNo']=int(input("Enter the book no. : "))
            d['Book_Name']=input("Enter the book name: ")
            d['Author']=input("Enter the author name: ")
            d['Price']=input("Enter the Price of the book: ")
            pickle.dump(d,f)
#CreateFile()
# ii) Write a function CountRec(Author) in python which accepts the author name as parameter  and count and return number of books 
#     by the given author are stored in the binary file "Book.dat"
def CountRec(author):
    ct_book=0
    with open('Book.dat','rb') as f2:
        try:
            while True:
                D=pickle.load(f2)
                if D['Author']==author:
                    ct_book+=1
        except EOFError:
            return ct_book
            f2.close()
#print(".....Check for the author and number of books produced.....")
#author=input("Enter the author name: ")
#print(CountRec(author))



# 2.Write a function that will display the first and second diagonal of a 2D list of 3 by 3 list .
# NOTe: fucntion will accept the list as parameter.
def func1(li):
    diag_1=list()
    diag_2=list()
    for i in range(0,len(li)-1):
        for j in range(0,len(li)-1):
            if(i==j):
                diag_1.append(li[i][j])
                if(i==1 and j==1):
                    diag_2.append(li[i][j])
            elif((i==2 and j==0) or (i==0 and j==2)):
                diag_2.append(li[i][j])
    print("FIRST DIAGONAL IS AS FOLLOWS: ",diag_1)
    print("SECOND DIAGONAL IS AS FOLLOWS: ",diag_2)
func1([[1,2,3],[4,5,6],[7,8,9]])


# 3. Elements of a list is 1,2,3. Write a function transfer() that will transfer the element of the L in a 2D list of 3 by 3 in such 
# a way that the resultant @D list will be like 
# 1 2 3
# 1 2 0
# 1 0 0

# 4. Write a fucntion that will display the sum of each coloumn of a 2D list of 3 by 3.

# 5. Amit has a list containing 10 integers. You need to help him create a program based on this list.
# i) Traverse the content of the list and push the even numbers into a stack.
# ii) Pop and display the content of the stack.

# 6. Write a function in python POP(Arr), where Arr is a stack implmented by a list of numbers. The function returns the value
# deleted from the stack.

# 7. Write a function that will transpose the element of a 2D list of 3 by 3 and display it in the matrix format.

# 8. Write a function in python that counts the number of 'Me' and "My" words present in a text file "Story.txt".

# 9. Write a function AMCount() in python, which should read each character of a text file Story.txt , should count and 
#    display the occurenence of A and M (including small cases of a and m too).

# 10. Write a method DISPLAYWORDS() in python to read lines from a text file STORY.TXT, and display those words, which are less than 
#     4 characters.

# 11. Write a function that will count the number of line starting with "A" from the text file ab.txt.

# 12. Write a function that will transfer all the lines start with "A" from A.txt to B.txt.  