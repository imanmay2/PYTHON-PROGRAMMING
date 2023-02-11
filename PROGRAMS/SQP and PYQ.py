# Write a method COUNTLINES() in python to read lines from the text file 'TESTFILE.TXT'  
# and display the lines which are not starting with any vowel.
def COUNTLINES():
    with open("TESTFILE.TXT") as f:
        v='aeiou'
        ct=0
        for i in f.readlines():
            if(i[0] in v):
                ct+=1
    return ct
# print("The number of lines not starting with any vowels: ",COUNTLINES())




# Write a function ETCount() in Python, which should read each character of a text file "TESTFILE.TXT" and then
# count and display the count of occurence of alphabets E and T insividually (including the small cases e and t too)
def ETCount():
    with open("TEST.TXT",'w') as f1:
        str2='Today is a pleasant day It might rain rain today It is mentioned on weather sites.'
        f1.write(str2)
    with open("TEST.TXT",'r') as f2:
        ct_t=0
        ct_e=0
        for i in f2.read():
            if(i=='e' or i=='E'):
                ct_e+=1
            elif(i=='t' or i=='T'):
                ct_t+=1
    print("E or e: ",ct_e)
    print("T or t: ",ct_t)
#ETCount()


# Write a function INDEX_LIST(L), where L is the list of elements passed as argument to the function. The function returns another list named 
# 'indexList' that stores the indices of all Non-Zero elements of L.
def INDEX_LIST(L):
    indexList=list()
    ct=-1
    for i in L:
        ct+=1
        if(i!=0):
            indexList.append(ct)
    return indexList
#print("The indexList will have: ",INDEX_LIST([12,4,0,11,0,56]))


# A list contains following record of a customer: 
# [Customer_name,Phone_number,City]
# Write the following user defined functions to perform given operations on the stack named status:
#   i) Push_element() - To push an object containing name and Phone number of customers who live in Goa to the stack
#   ii) Pop_element()- To Pop the objects from the stack and display them. Also, display" stack empty"
#        when there are no  elements in the stack.
'''For example:
If the lists of customer details are:
[“Gurdas”, “99999999999”,”Goa”]
[“Julee”, “8888888888”,”Mumbai”]
[“Murugan”,”77777777777”,”Cochin”]
[“Ashmit”, “1010101010”,”Goa”]
The stack should contain
[“Ashmit”,”1010101010”]
[“Gurdas”,”9999999999”]
The output should be:
[“Ashmit”,”1010101010”]
[“Gurdas”,”9999999999”]
Stack Empty'''

def push(stk):
	li=list()
	n=int(input("Enter the range: "))
	for i in range(n):
		name=input("Enter the name: ")
		phn_no=int(input("Enter the phone number: "))
		city=input("Enter the city: ")
		li.append(name)
		li.append(phn_no)
		li.append(city)
		if(city.lower()=='goa'):
			stk.append(li)
def pop(stk):
	if(stk==[]):
		print("Stack Empty!!")
	else:
		print(stk.pop())
def menu():
	print("MENU")
	print("1. PUSH")
	print("2. POP")
	print("3.EXIT")
	stk=list()
	ans='yes'
	while ans=="yes":
		ch=int(input("Enter your choice: "))
		if(ch==1):
			push(stk)
		elif(ch==2):
			pop(stk)
		elif(ch==3):
			print("bye bye!!")
			break
		else:
			print("please enter a valid choice from 1 to 3")

# Write a fucntion in python, Push(SItem) where, SItem is a dictionary conataining the details of stationary items- {Snamne: price}
# The function should push the names of those items in the stack who have the price greater than 75. Also display the count of elements
#pushed into the stack.
def Push(SItem):
    ct=0
    st=list()
    for i in SItem:
        if(SItem[i]>75):
            ct+=1
            st.append(i)
    return ct
#print("STACK IMPLEMENTED SUCCESSFULLY!!")
#print("COUNT OF THE NAME IMPLEMENTED ARE: ",Push({'Manmay':78,'Anwesha':80,'Soumya':34,'Lopa':78}))

# FILL IN THE BLANKS:
# i)
import mysql.connector as mysql
def sql_data():
    con1=mysql.connect(host="localhost",user="root",password="tiger", database="school")
    mycursor=con1.cursor()#Statement 1 
    rno=int(input("Enter Roll Number :: "))
    name=input("Enter name :: ")
    clas=int(input("Enter class :: "))
    marks=int(input("Enter Marks :: "))
    querry="insert into student values({},'{}',{},{})".format(rno,name,clas,marks)
    mycursor.execute(querry) #Statement 2
    con1.commit() #Statement 3
    print("Data Added successfully")

# ii)
import mysql.connector as mysql
def sql_data():
 
    con1=mysql.connect(host="localhost",user="root",password="tiger", database="school")
    mycursor=con1.cursor()#Statement 1
    print("Students with marks greater than 75 are : ")
    mycursor.execute("select * from school where marks>75;")
    data=mycursor.fetchall() #Statement 3
    for i in data:
        print(i)
    print()

#iii)
'''import pickle #Statement 1
def update_data():
    rec={}
    fin=open("record.dat","rb") 
    fout=open("temp.dat","wb") #Statement 2
    found=False
    eid=int(input("Enter employee id to update their salary :: "))
    while True:
        try:
            rec=pickle.load(fin)#Statement 3
            if rec["Employee id"]==eid:
                found=True 
                rec["Salary"]=int(input("Enter new salary :: "))
                pickle.dump(rec,fout)#Statement 4
            else:
                pickle.dump(rec,fout)
        except:
            break
    if found==True:
    print("The salary of employee id ",eid," has been updated.")
    else:
    print("No employee with such id is not found")
    fin.close()
    fout.close()'''





#								YEAR: 2019




# WRITE A FUNCTION  RevvText() TO READ A TEXTFILE "INPUT.TXT" AND PRINT ONLY WORD STARTING WITH I IN REVERSE ORDER.
# E.G: INPUT:  INDIA IS MY COUNTRY.
#	OUTPUT: AIDNI SI MY COUNTRY.
def write_input():
	with open("book.txt","w") as i2:
		i2.write("INDIA hii")
def RevText():
	with open("Input.txt") as i1:
		str1=''
		for i in i1.read().split():
			if(i[0]=='i' or i[0]=='I'):
				str1=str1+i[::-1]+' '
			else:
				str1+=i+' '
		print(str1)
#write_input()
#RevText()


#WRITE A FUNCTION TO COUNT THE NUMBER OF LOWERCASE ALPHABETS PRESENT IN A TEXT FILE BOOK.TXT.

def count_lowercase():
	with open("book.txt") as i3:
		ct=0
		for i in i3.read():
			if(i.islower()):
				ct+=1
	print("count of the lowercase: ",ct)
#count_lowercase()




#								YEAR: 2017




#WRITE A METHOD  IN PYTHON TO READ LINES FROM A TEXT FILE "MYNOTES.TXT". AND DISPLAY THOSE LINES, WHICH ARE STARTING WITH THE APLHABET-'K'
def display_k():
	with open("MYNOTES.TXT") as i4:
		for i in i4.readlines():
			if(i[0]=='k' or i[0]=='K'):
				print(i)

#display_k()


#								YEAR: 2016

# Write a method that will find and display the prime numbers between 2 to N. Pass N as argument to the method.
def prime(N):
	for i in range(2,N+1):
		ct=0
		for j in range(2,i+1):
			if(i%j==0):
				ct+=1
		if(ct==1):
			print(i,end=',')
#prime(int(input("Enter the range : ")))




# Write a method  in python to write multiple line of text contents into a text file daynote.txt.
def write_multiline():
	with open("daynote.txt",'w') as i5:
		ans='y'
		while ans=='y':
			i5.write(input("Enter the line: ")+'\n')
			ans=input("Are there more line to be written y/n: ")
#write_multiline()



# CONSIDER THE FOLLOWING DEFINATION OF CLASS EMPLOYEE, WRITE A METHOD IN PYTHON TO SEARCG AND DISPLAY THE CONTENT IN A PICKLED FILE EMP.DAT
# WHERE EMPNO IS MATCHING WITH 'A0005'.
import pickle 
def search():
	with open("emp.dat") as i6:
		try:
			while True:
				k=pickle.load(i6)
				if(k['Employee']=='A0005'):
					print(k)
		except EOFError:
			i6.close()




#								YEAR: 2015



# write a method in python to display the elements of list twice. if it is a no. and display the element terminated with * if it is not a 
# number.
def display(li):
	for i in li:
		if(type(i)==type(1)):
			print(str(i)+str(i))
		elif(type(i)==type('s')):
			print(i+'*')
#display(['RAMAN',21,'YOGRAJ',3,'TARA'])




#Write PUSH(Names) and POP(Name) methods in python to add names
#and remove names considering them to act as push and pop
#operation in stack

def PUSH(Name,n):
	if(len(Name)!=n):
		Name.append(input("Enter the name : "))
	else:
		print("STACK OVERFLOW!!")
def POP(Name):
	if(Name==[]):
		print("Stack empty!!")
	else:
		print(Name.pop())
def disp(): 
	print("MENU") 
	print("1.PUSH") 
	print("2.POP") 
	ans='y'
	Name=list()
	n=int(input("Enter the length of the list of the names: "))
	while ans=='y':
		ch=int(input("Enter your choice: "))
		if(ch==1):
			PUSH(Name,n)
		elif(ch==2):
			POP(Name)
		elif(ch==3):
			print('bye ! bye!')
			break
		ans=input("Wanna continue: y/n: ")
#disp()




# WRITE A FUNCTION  THAT WILL DISPLAY THE COMPOSITE NUMBER FROM 2 TO N.(n must be accepted by the user)
def composite(N):
	for i in range(1,N+1):
		ct=0
		for j in range(1,i+1):
			if(i%j==0):
				ct+=1
		if(ct!=2):
			print(i)
#composite(int(input("Enter the range upto which it will print the composite number: ")))


