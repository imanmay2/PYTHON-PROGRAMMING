import random
sc=0
su=0
print("GAME BEGINS FROM HERE......")
print("KEEP IN MIND TOTAL POINTS IS 16..AND YOUR SCORE WILL BE CALCULATED BASES UPON THAT....")
print("BEST OF LUCK.................")
def game(user,comp):
    if(user=="R" and comp=="P"):
        sc=sc+1
    elif(user=="P" and comp=="S"):
        sc=sc+1
    elif(user=="S" and comp=="R"):
        sc=sc+1
    elif(user=="P" and comp=="R"):
        su=su+1
    elif(user=="S" and comp=="P"):
        su=su+1
    elif(user=="R" and comp=="S"):
        su=su+1
for i in range(1,17):
    user=input("please enter any one of the following:- R(ROCK), P(PAPER) AND S(SCISSOR)")
    r=random.randint(1,3)
    if(r==1):
        comp="R"
    elif(r==2):
        comp="P"
    elif(r==3):
        comp="S"
    print("You have choosen",user)
    print("computer have choosen",comp)
    game(user,comp)
print("YOUR TOTAL SCORE OUT OF 16 IS",su)
print("COMPUTER'S  TOTAL SCORE OUT OF 16 IS",sc)

