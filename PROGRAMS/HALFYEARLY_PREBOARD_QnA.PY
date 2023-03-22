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




######### 3. Elements of a list is 1,2,3. Write a function transfer() that will transfer the element of the L in a 2D list of 3 by 3 in such 
# a way that the resultant @D list will be like 
# 1 2 3
# 1 2 0
# 1 0 0
def Transfer(l):
	li=list()
	for i in range(0,len(l)):
		if(i==0):
			li.extend([l])
		else:
			l[len(l)-i]=l[len(l)-i]-l[len(l)-i]
			li.extend([l])
	print(li)
Transfer([1,2,3])			
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
def Transpose_matrix(li):
	for i in range(0,len(li)):
		for j in range(0,len(li)):
			li[i][j]=li[j][i]
	print('[')
	for i in li:
		print(i)
	print(']')
##Transpose_matrix([[1,2,3],[4,5,6],[7,8,9]])


# 8. Write a function in python that counts the number of 'Me' and "My" words present in a text file "STORY.txt".
def func8():
	with open("Story.txt",'r') as f8:
		ct_me=0
		ct_my=0
		for i in f8.read().split():
			if(i=='Me'):
				ct_me=ct_me+1
			elif(i=='My'):
				ct_my=ct_my+1
		print("Count of Me and My are : ",ct_me,ct_my,"respectively")
#func8()




# 9. Write a function AMCount() in python, which should read each character of a text file Story.txt , should count and 
#    display the occurenence of A and M (including small cases of a and m too).
def AMCount():
	with open("Story.txt",'r') as f9:
		ct_m=0
		ct_a=0
		for i in f9.read():
			if(i=='A' or i=='a'):
				ct_a+=1
			elif(i=='M' or i=='m'):
				ct_m+=1
		print("Count of A and M including small letters are : ",ct_a,ct_m,"respectively")	
#func9()




# 10. Write a method DISPLAYWORDS() in python to read lines from a text file Story.TXT, and display those words, which are less than 
#     4 characters.
def DISPLAYWORDS():
	with open('Story.txt') as f10:
		print("WORDS WHICH ARE LESS THAN 4 CHARACTERS ARE AS FOLLOWS : ")
		for i in f10.read().split():
			if(len(i)<4):
				print(i,end=' ')
#DISPLAYWORDS()
# 11. Write a function that will count the number of line starting with "A" from the text file Story.txt.
def func11():
	with open('Story.txt') as f11:
		ct=0
		for i in f11.readlines():
			if(i[0]=='A'):
				ct+=1
		print("Number of lines starting with A are : ",ct)
#func11()
		
	


# 12. Write a function that will transfer all the lines start with "A" from A.txt to B.txt.  
def func12():
	with open("A.txt",'r') as f12:
			with open("B.txt",'w') as f121:
				for i in f12.readlines():
					if(i[0]=='A'):
						f121.write(i)
#func12()




							# PRE-BORADS QUESTION PAPER


#13.  Write a method COUNTLINES() in python to display the number of lines from the text file 'TESTFILE.TXT'
#     and transfer the lines which are not started with any vowel to another 'C.TXT'.
def COUNTLINES():
	ct_total=0
	v='AEIOUAaeiou'
	with open('TESTFILE.TXT','r') as f131:
		print("TOTAL NUMBER OF LINES PRESENT IN TESTFILE.TXT ARE : ",len(f131.readlines()))
		with open('c.txt','w') as f132:
			for i in f131.realines():
				if(i[0] not in v):
					f132.write(i)
#COUNTLINES()


		
#14.  Write a function ETCount() in python, which should read each character of a text file 'TESTFILE.TXT'
#     and then count and display the count the occurence of the alphabets E and T individually (including small cases and e and t too).
def ETCount():
	ct_e=0
	ct_t=0
	with open('TESTFILE.TXT','r') as f14:
		for i in f14.read():
			if(i=='e' or i=='E'):
				ct_e+=1
			elif(i=='t' or i=='T'):
				ct_t+=1
		print("COUNT OF E AND T ARE : ",ct_e,ct_t,"RESPECTIVELY")
#ETCount()

	


#15.  Write a fucntion in python , Push(SItem) where, SItem is a dictionary containing the details of stationary items- {Sname:price}.
#     The function should push the names of those items in the stack who have price greater than 75. Also, display the count of elements 
#     pushed into the stack.
def Push(SItem):
	ct_stk=0
	stk=list()
	for i in SItem:
		if(SItem[i]>75):
			ct_stk+=1
			stk.append(i)
	print("STACK IS AS FOLLOWS :  ",stk)
	print("COUNTS OF THE ELEMENTS PUSHED INTO THE STACK ARE : ",ct_stk)
#Push({'Rajveer':45,'Vutu':96})




#16.  Write a function INDEX_LIST(L), where L is the list of elements passed as argument to the function.
#     The fucntion returns another list named 'indexList' that stores the indices of all the even elements of L.
def INDEX_LIST(L):
	indexList=list()
	for i in L:
		if(i%2==0):
			indexList.append(L.index(i))
	return indexList
print(INDEX_LIST([1,2,3,4,5,6,7,8,9,0]))




#17.  Write a Program in Python that defines and calls the following user defined functions: 
#           add()- To accept and add data of an employee to a CSV file 'furdata.csv'.
#                  Each records contains of a list with field elements as fid,fname,and fprice to store furniture name and furniture price
#                  respectively..
#        search()- To display the records of the furniture whose price is more than 10000.



#18.  Write a function Lshift(Arr,n) in python, which accepts a list Arr of numbers and n is a numeric value by which all elements are shifted to left.



#19.  Write a function that counts the numbers of 'Me' and 'My' words present in a text file 'STORY,TXT'     
def func19():
    ct_Me=0
    ct_My=0
    with open('STORY.TXT','r') as f19:
        for i in f19.read().split():
            if(i=='Me'):
                ct_Me+=1
            elif(i=='My'):
                ct_My+=1
        print("COUNT OF ME AND MY ARE : ",ct_Me,ct_My,"RESPECTIVELY")
#func19()


#20.  Write a function that reads a text file line by line and display each words separated by #.
def func20():
    with open('Story.txt') as f20:
        for i in f20.read().split():
            print(i,end='#')
#func20



#21. Write a function that reads a text file and display the number of uppercase and lowercase characters in the file.
def func21():
    with open('Story.txt') as f21:
        ct_upp=0
        ct_low=0
        for i in f21.read():
            if(i.isupper()):
                ct_upp+=1
            elif(i.islower()):
                ct_low+=1
	print('NUMBER OF UPPERCASE AND LOWERCASE CHARACTERS ARE : '.ct_upp,ct_low,'RESPECTIVELY')
#func21()
#22.  Remove all the lines that contain the character 'a' in a file and write it to another file.
def func22():
	with open('Story.txt','r') as f221:
            with open('Write.txt','w') as f222:
                for i in f221.readlines():
                    if('a' in i):
                        f222.write(i)


#23.  Create a binary file with the name and roll number. Search for a given roll number and display the name, if not found display appropriate message.
import pickle
def func23_create():
    with open('bin.dat','wb') as f231:
        d=dict()
        n=int(input("Enter the range : "))
        for i in range(n):
            d['Name']=input("Enter the name of the student : ")
            d['Roll']=int(input("Enter the Roll no. : "))
            pickle.dump(d,f231)
f23_create()
def func23_search():
    with open('bin.dat','rb') as f232:
		print(pickle.load(f232))
f23_search()
