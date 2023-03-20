import threading as t
def sq(s):
    print('sleeping for 4 seconds',time.sleep(s))
    print('sleeping for 2 seconds',time.sleep(s-2))
def cube(num):
    for i in range(2,num-1):
        print(i**3,end=',')
t1=t.Thread(target=sq,args=(6,))
t2=t.Thread(target=cube,args=(8,))
t1.start()
t2.start()
