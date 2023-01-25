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
#   i) Push_element() - To ush andobject containing name and Phone number of customers who live in Goa to the stack
#   ii) Pop_element()- To Pop the objects from the stack and display them. Also, display" stack empty"
#        when there are no  elemetns in the stack.



# Write a fucntion in python, Push(SItem) where, SItem is a dictionary conataining the details of stationary items- {Snamne: price}
# The function shopuld push the names of those items in the stack who have the price greater than 75. Also display the count of elements
#pushed into the stack.
