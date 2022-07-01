q=["who is the first president of india","what is a nuetral number?","what is the full form of WWW?","enter the largest negative number","enter the first 3 digit largest prime number?"]
a=["rajendra prasad","zero or 0","world wide web","minus one or -1","nine hundred ninety seven or 997"]
print("YOUR QUIZ BEGINS NOW")
score=0
for i in range(0,5):
    print(q[i])
    ans=input("enter the answer of the above question printed").lower()
    if(ans in a[i]):
        score=score+1
print("QUIZ ENDS.........")
print("the score of your Quiz is",score)