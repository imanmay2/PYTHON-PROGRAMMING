#to print the frequrncy of each word in a file and store it in a new one.
import json
with open("donkey.txt") as f:
    sentence=f.read()
    words=sentence.split()
    d={}
    with open("Frequency.txt","w") as f1:
        for i in words:
            key=i
            if(key not in d):
                count=words.count(key)
                d[key]=count
        f1.write("Frequency of the words are")
        f1.write(json.dumps(d,indent=1))
        
