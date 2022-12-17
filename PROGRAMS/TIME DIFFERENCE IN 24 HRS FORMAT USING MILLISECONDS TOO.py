import datetime
def d_time(n1,n2):
    return(datetime.timedelta(hours=int(n2.split(":")[0]), minutes=int(n2.split(":")[1]), seconds=int(n2.split(":")[2])+ int(n2.split(":")[3])/1000) - datetime.timedelta(hours=int(n1.split(":")[0]), minutes=int(n1.split(":")[1]), seconds=int(n1.split(":")[2])+ int(n1.split(":")[3])/1000))    
n1=input("Enter the time in 24 hrs format: ")
n2=input("Enter the time in 24 hrs format: ")
print(d_time(n1,n2))
