with open("poem1.txt") as f:
    str1=f.read()
    v="AEIOUaeiou"
    vo=0
    co=0
    for i in str1:
        if(i in v):
            vo+=1
        else:
            co+=1
    print("COUNT OF VOWEL AND CONSONANT IS: ",vo,co,"RESPECTIVELY")