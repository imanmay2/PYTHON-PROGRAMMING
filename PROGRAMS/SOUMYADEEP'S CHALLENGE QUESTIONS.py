#1.Store userInp data other than  in a list and array.
def func1():
    inp=''
    ans='y'
    while(ans=='y'):
        item=input("Enter the item to be stored: ")
        inp=inp+item+','
        ans=input("Wanna store more datas?? y/n?? ")
    print("Datas which are stored is: ")
    for i in inp.split(','):
        print(i,end=',')


#2. WAP to convert infix to postfix and reverse of it.
#3. WAP to check precedence order of operators. Eg. Input => * and + … Output => * is in higher preceedance.
#   Eg: Input => * and / Out[ut => Same preceedance …
#4. WAP to display output in tabular format
#   (as we see in MySQL output of select command) for inputs by user.
