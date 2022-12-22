#IMPLEMENTATION OF THE STACK OPERATION................

def push(stk,item,n):
    if(len(stk)==n):
        print("Overflow")
    else:
        stk.append(item)
def pop(stk):
    if(stk==[]):
        print("Stack is empty")
    else:
        print("Poped element of the stack is: ",stk.pop())
def peek(stk):
    if(stk==[]):
        print("Stack is empty")
    else:
        print("Peek value of the stack: ",stk[len(stk)-1])
def display(stk):
    if(stk==[]):
        print("stack is empty")
    else:
        print("stack is as follows: ")
        for i in range(len(stk)-1,-1,-1):
            print(stk[i])
# main code starts now.........
stk=[]
n=int(input("Enter the strength of the stack: "))
while True:
    print("STACK OPERATIONS")
    print("1. PUSH")
    print("2. POP")
    print("3. PEEK")
    print("4. DISPLAY STACK")
    print("5. EXIT!!")
    ch=int(input("Enter the choice: "))
    if(ch==1):
        item=int(input("Enter the item to be pushed into the stack: "))
        push(stk,item,n)  
    elif(ch==2):
        pop(stk)
    elif(ch==3):
        peek(stk)
    elif(ch==4):
        display(stk)
    elif(ch==5):
        print("BYE BYE!!!!")
        break
    else:
        print("INAVALID INPUT!!!PLEASE ENTER FROM 1 TO 5!!!! TRY AGAIN AFTER SOMETIME!!!")  


# IMPLEMENTATION OF THE  QUEUES OPERATIONS...........
def enque(Qu,item,n):
    if(len(Qu)==n):
        print("Overflow")
    else:
        Qu.append(item)
def pop(Qu):
    if(Qu==[]):
        print("Queues is empty")
    else:
        print("Poped element of the Queues is: ",Qu.pop())
def peek(Qu):
    if(Qu==[]):
        print("Queue is empty")
    else:
        print("Peek value of the Queues: ",Qu[len(Qu)-1])
def display(Qu):
    if(Qu==[]):
        print("Queues is empty")
    else:
        print("Queues is as follows: ")
        for i in range(len(Qu)-1,-1,-1):
            print(Qu[i])
# main code starts now.........
Qu=[]
n=int(input("Enter the strength of the Qu: "))
while True:
    print("Queues OPERATIONS")
    print("1. ENQUEUE")
    print("2. DEQUEUE")
    print("3. TOPMOST VALUE")
    print("4. DISPLAY QUEUES")
    print("5. EXIT!!")
    ch=int(input("Enter the choice: "))
    if(ch==1):
        item=int(input("Enter the item to be enqueue into the Queue: "))
        push(Qu,item,n)  
    elif(ch==2):
        pop(Qu)
    elif(ch==3):
        peek(Qu)
    elif(ch==4):
        display(Qu)
    elif(ch==5):
        print("BYE BYE!!!!")
        break
    else:
        print("INAVALID INPUT!!!PLEASE ENTER FROM 1 TO 5!!!! TRY AGAIN AFTER SOMETIME!!!")  