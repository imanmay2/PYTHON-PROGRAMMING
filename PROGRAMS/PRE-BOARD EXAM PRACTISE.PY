#                       HALF YEARLY QUESTION PAPER
#1. Write a fucntion in python that counts the number of "Me" or "My" words present in a text file "STORY.TXT".
def func1():
    with open("STORY.TXT") as f:
        ct_Me=ct_My=0
        for i in f.readlines():
            if "Me" in i:
                ct_Me+=1
            elif "My" in i:
                ct_My+=1
        print("Count of Me: ",ct_Me)
        print("Count of My: ",ct_My)
func1()

#2. 