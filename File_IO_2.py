def game():
    return inp
inp=input("Enter your score")
score=game()
with open("highscore.txt") as f:
    highscore=f.read()
if(score>highscore):
    with open("highscore.txt","w") as f1:
        f1.write(score)
