#wap that will take date from the user return yesterday or anything else..
from datetime import date
def calc(inp:str)->str:
    inp=inp.split('-')
    def leap(year):
        if(year%100==0 and year%400==0):
            return True
        elif(year%100==0 and year%400!=0):
            return False
        elif(year%4==0):
            return True
        else:
            return False

    #t=str(date.today()).split('-')
    t=["2020","11","01"]
    li_months=["January","February","March","April","May","June","July","August","September","October","November","December"]
    if(t[0]==inp[0]) and leap(int(inp[0])) and t[1]=='03' and inp[1]=='02' and t[2]=='01' and inp[2]=='29':
        return ("Yesterday")
    elif(t[0]==inp[0]) and not leap(int(inp[0])) and t[1]=='03' and inp[1]=='02'  and t[2]=='01' and inp[2]=='28':
        return "Yesterday"
    elif(((t[2]=='01' and inp[2]=='31') or (t[2]=='01' and inp[2]=='30'))and t[0]==inp[0] and int(t[1])-1==int(inp[1])):
        return ("Yesterday")
    elif(int(t[2])-1==int(inp[2]) and t[0]==inp[0] and t[1]==inp[1]):
        return ("Yesterday")
    else:
        return inp[2]+" "+li_months[int(inp[1])-1]+" "+inp[0]
inp=input("ENTER YOUR DESIRED DATE: ")
print(calc(inp))
# 2020-03-01
# 2020-02-29
