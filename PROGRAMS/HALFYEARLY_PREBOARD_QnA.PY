#                                                       HALF-YEARLY QUESTION PAPER
# 1. A binary file ''Book.dat" has structure [BookNo,Book_Name,Author,Price].
# i) Write a user defined function CreateFile() to input for a recorde and add to Book.dat
import pickle
def CreateFile():
    with open("Book.dat","wb") as f:
        d=dict()
        n=int(input("Enter how many inputs : "))
        for i in range(n):
            d['BookNo']=int(input("ENTER THE BOOK NUMBER : "))
            d['Book_Name']=input("ENTER THE BOOK NAME : ")
            d['Author']=input("ENTER THE AUTHOR NAME : ")
            d['Price']=input("ENTER THE PRICE OF THE BOOK : ")
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
#print(".....CHEECKING FOR THE AUTHOR AND THE NUMBER OF BOOKS PRODUCED.....")
#author=input("ENTER THE AUTHOR NAME: ")
#print(CountRec(author))



# 2.Write a function that will display the first and second diagonal of a 2D list of 3 by 3 list .
# NOTe: fucntion will accept the list as parameter.
def func2(li):
    diag_1=list()
    diag_2=list()
    for i in range(0,len(li)):
        for j in range(0,len(li)):
            if(i==j):
                diag_1.append(li[i][j])
                if(i==1 and j==1):
                    diag_2.append(li[i][j])
            elif((i==2 and j==0) or (i==0 and j==2)):
                diag_2.append(li[i][j])
    print("FIRST DIAGONAL IS AS FOLLOWS: ",diag_1)
    print("SECOND DIAGONAL IS AS FOLLOWS: ",diag_2)
#func2([[1,2,3],[4,5,6],[7,8,9]])


# 3. Elements of a list is 1,2,3. Write a function transfer() that will transfer the element of the L in a 2D list of 3 by 3 in such 
# a way that the resultant @D list will be like 
# 1 2 3
# 1 2 0
# 1 0 0

# 4. Write a fucntion that will display the sum of each coloumn of a 2D list of 3 by 3.
def func4(li):
	s1=s2=s3=0
	for i in range(0,len(li)):
		if(i==0):
			s1=s1+sum(li[i])
		elif(i==1):
			s2=s2+sum(li[i])
		elif(i==2):
			s3=s3+sum(li[i])
	print("SUM OF THE 1ST COLOUMN IS: ",s1)
	print("SUM OF THE 2ND COLOUMN IS: ",s2)
	print("SUM OF THE 3RD COLOUMN IS: ",s3)
#func4([[1,2,3],[4,5,6],[7,8,9]])




# 5. Amit has a list containing 10 integers. You need to help him create a program based on this list.
# i) Traverse the content of the list and push the even numbers into a stack.
def func5_pusheven(li,stk):
	for i in li:
		if i%2==0:
			stk.append(i)
# ii) Pop and display the content of the stack.
def func5_pop(stk):
	if(stk!=[]):
		print("ELEMENT POPED OUT FROM THE STACK IS : ",stk.pop())
	elif(stk==[]):
		print("!!!!STACK EMPTY!!!!")
def func5_display(stk):
	if stk==[]:
		print("!!!!STACK EMPTY!!!!")
	else:
		stk=stk[::-1]
		for i in stk:
			print(i)
stk=list()
#li=eval(input("ENTER THE LIST OF 10 : "))
#func5_pusheven(li,stk)
#func5_pop(stk)
#print("ELEMENTS IN THE STACK ARE : ")
#func5_display(stk)




# 6. Write a function in python POP(Arr), where Arr is a stack implemented by a list of numbers. The function returns the value
# deleted from the stack.
def func6_push(stk):
	n=int(input("HOW MANY NUMBERS YOU WANT TO ENTER : "))
	for i in range(n):
		num=int(input("ENTER THE ELEMENT TO BE PUSHED IN THE STACK : "))
		stk.append(num)
def func6_pop(stk):
	if(stk==[]):
		print("__________STACK EMPTY________")
	else:
		return stk.pop()
stk=list()
#func6_push(stk)
#print("ELEMENTS POPED OUT FROM THE STACK IS : ",func6_pop(stk))





# 7. Write a function that will transpose the element of a 2D list of 3 by 3 and display it in the matrix format.

# 8. Write a function in python that counts the number of 'Me' and "My" words present in a text file "STORY.txt".
def func8():
	with open("STORY.txt") as f8:
		ct_me=0
		ct_my=0
		for i in f8.read():
			if(i=='Me'):
				ct_me=ct_me+1
			elif(i=='My'):
				ct_my=ct_my+1
		print("Count of Me and My are : ",ct_me,ct_my,"respectively")
#func8()
# 9. Write a function AMCount() in python, which should read each character of a text file Story.txt , should count and 
#    display the occurenence of A and M (including small cases of a and m too).

# 10. Write a method DISPLAYWORDS() in python to read lines from a text file STORY.TXT, and display those words, which are less than 
#     4 characters.

# 11. Write a function that will count the number of line starting with "A" from the text file ab.txt.

# 12. Write a function that will transfer all the lines start with "A" from A.txt to B.txt.  
