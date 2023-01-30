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
def insert(li):
    for i in range(4):
        l=list()
        name=input("Enter the name of the customer: ")
        ph_no=int(input("Enter the phone no. of the customer: "))
        city=input("Enter the city: ")
        l.append(name)
        l.append(ph_no)
        l.append(city)
        li.append(l)
def push(stk,n,li):
    for i in range(0,len(li)-1):
        if(li[i][2]=="Goa"):
            stk.append(li[i])
            if(len(stk)==n):
                print("STACK OVERFLOW")
                break
def pop(stk):
    if(stk==[]):
        print('STACK EMPTY')
    elif(stk!=[]):
        print("POPED OUT ELEMENT IS",stk.pop())
        
def main():
    li=list()
    stk=list()
    insert(li)
    ans='y'
    while ans=='y':
        print("ENTER YOUR CHOICE: ")
        print("1.PUSH")
        print("2. POP")
        ch=int(input("Enter your choice: "))
        if(ch==1):
            n=int(input("Enter the total range of the stack: "))
            push(stk,n,li)
        elif(ch==2):
            pop(stk)
        else:
            print("INVALID CHOICE!!!! PLEASE SELECT A VALID ONE !!!!")
        ans=input("Wanna continue???? y/n: ")
main()

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

