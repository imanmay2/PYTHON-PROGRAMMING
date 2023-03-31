def transpose(original:list)->list:
    transposed=[]
    for i in range(len(original[0])):
        temp_list=[]
        for j in range(len(original)):
            temp_list.append(original[j][i])
        transposed.append(temp_list)
    return transposed
def Push(SItem):
    stk=list()
    ct=0
    for i in SItem:
        if(SItem['price']>75):
            stk.append(i)
            ct+=1
    print(ct,stk)
import csv
def add():
    with open("furdata.csv",'w',newline='') as f1:
        li=list()
        n=int(input("Enter then range : "))
        stuwriter=csv.writer(f1,delimiter='|')
        stuwriter.writerow(['fid','fname','fprice'])
        for i in range(n):
            l=[]
            fid=input("Enter id : ")
            fname=input("Enter the name : ")
            fprice=float(input("Enter the price : "))
            l.append(fid)
            l.append(fname)
            l.append(fprice)
            li.append(l)
        stuwriter.writerows(li)
def search():
    with open('furdata.csv','r',newline='\r\n') as f:
        r=csv.reader(f)
        print('Records which are having price more than 10000 :')
        for i in r:
            if((i[0].split('|')[2])>10000):
                print(i)

import pickle
def binary():
    with open('pickl.bin','wb') as f3:
        n=int(input("Enter the range : "))
        d=dict()
        for i in range(n):
            d['name']=input("Enter name : ")
            d['roll']=int(input("Enter the roll : "))
            pickle.dump(d,f3)
    with open('pickl.bin','rb') as f4:
        try:
            f=False
            while True:
                D=pickle.load(f4)
                if(D['roll']==2):
                    print(D)
                    f=True
        except EOFError:
            if(f==True):
                print('Result found!! Search successful!!')
            else:
                print("Result not found")

def print_(a,b=9):
    print(a,b)


def mysql():
    import mysql.connector as s
    mycon=s.connect(host='localhost',user='root',database='hello',passwd='2%0*2)0$Happy')
    if(mycon.is_connected()):
        print('PYTHON IS CONNECTED WITH MYSQL')
        cursor=mycon.cursor()
        cursor.execute("select * from trainer where city not in('%s')"%('CHENNAI'));
        data=cursor.fetchall()
        for i in data:
            print(i)
mysql()
    
