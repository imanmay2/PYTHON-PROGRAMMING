#               ....DEVELOP A BOT....
## Accept input from user and BOT should answer accordingly.
question=["what's my name","who are you","when is your birthday","what is python","sleep"]
answer=["Hacker","Hacker's BOT","27th December 2021","Python is open source project","Thank You"]
while(1):
    q=input(".......Enter your question......").lower()
    if(q in question):
        li=question.index(q)
        print("Answer : ",answer[li])
        if(li==4):
            break
    else:
        print("Question not found in our list!!!")
    



