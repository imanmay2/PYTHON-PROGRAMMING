import DIFFTIME as t
t1=int(input("ENTER THE TIME 1 IN MILLITARY FORMAT : "))
d1=input("ENTER THE DATE PLEASE : ").upper().split()
t2=int(input("ENTER THE TIME 2 IN MILLITARY FORMAT : "))
d2=input("ENTER THE DATE PLEASE : ").upper().split()
d_diff=int(d1[0])-int(d2[0])
if(d_diff<0):
    d_diff*=(-1)
t.time_diff_date(t1,t2,d_diff)

