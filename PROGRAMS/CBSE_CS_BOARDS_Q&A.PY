#CBSE.....2023 ....SET 4 .....PYTHON PROGRAMS SOLUTION....


#Q>(27)(a) SOLUTION
def LongLines():
    with open('lines.txt','r') as f1:
        for i in f1.readlines():
            if(len(i.split())>9):
                print(i)
#LongLines()


# Q(27)(b) SOLUTION
def count_Dwords():
    dig='0123456789'
    ct=0
    with open('Details.txt','r') as f2:
        for i in f2.readlines():
            for j in i.split():
                if(j[len(j)-1] in dig):
                    ct+=1
    print("Number of words ending with a digit are : ",ct)
#count_Dwords()      
                


# Q(29) SOLUTION
def EOReplace(L):
    li=list()
    for i in L:
        if(i%2==0):
            li.append(i+1)
        elif(i%2!=0):
            li.append(i-1)
    print("List after replacing is : ",li)
#EOReplace([10,20,30,40,35,55])
            


#Q) (30)(a) SOLUTION



# Q)(30) (b) SOLUTION
def Push(Vehicle):
    stk=list()
    for i in Vehicle:
        if(Vehicle[i].lower()=='tata'):
            stk.append(i)
    if(stk==[]):
        print('Stack is empty')
    else:
        print("Stack is as follows")
        for i in stk:
            print(i)
#Push({'Santro':'Hyundai','Nexon':'TATA','Safari':'TaTa'})



#Q) 33) (A)
