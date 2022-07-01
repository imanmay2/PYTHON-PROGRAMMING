# wap accept three subject marks calculayee% marks and display grade as per

#80-100    a
#60-79       b
#from 40 - 60 c
#below 40    f
a=float(input("enter the first subjects"))
b=float(input("enter the second subjects"))
c=float(input("enter the third subjects"))
per=((a+b+c)*100)/300
if(per>=80 and per<=100):
    print("grade A")
elif(per>=60 and per<80):
    print("grade B")
elif(per>=40 and per<60):
    print("garde C")
else:
    print("grade D")
