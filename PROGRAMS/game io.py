sc=int(input("enter your score"))
def game():
    return sc
score=game()
with open("high score.txt","r") as f:
    if(f.read()<str(score) or f.read()==""):
        f1=open("high score.txt","w")
        f1.write(str(score))
        f1.close()
        

