def time_diff(t1,t2):
    diff=((t1//100)*60+(t1%100))-((t2//100)*60+(t2%100))
    if(diff<0):
        diff*=(-1)
    print(diff//60," HOURS ",diff%60," MINS ")
def time_diff_date(t1,t2,d_diff):
    diff=((t1//100)*60+(t1%100))-((t2//100)*60+(t2%100))
    if(diff<0):
        diff*=(-1)
    net_t=d_diff*24*60
    diff=net_t-(diff*d_diff)
    print(diff//60," HOURS ",diff%60," MINS ")
    