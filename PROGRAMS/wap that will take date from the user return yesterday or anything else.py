#wap that will take date from the user return yesterday or anything else..
from datetime import date
def calc(inp):
    t=str(date.today()).split('-')
    li_months=["January","February","March","April","May","June","July","August","September","October","November","December"]
    if(int(t[2])-1==int(inp[2])):
        return ("Yesterday")
    else:
        return int(inp[2]),li_months[int(inp[1])-1],int(inp[0])


inp=input("ENTER YOUR DESIRED DATE: ").split('-')
print(calc(inp))
