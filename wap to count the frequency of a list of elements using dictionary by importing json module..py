# wap to count the frequency of a list of elements using dictionary by importing json module.
import json
sentence=input("enter the sentences which contains certains list of words")
d={}
words=sentence.split()
for i in words:
    key=i
    if(key not in d):
        ct=words.count(key)
        d[key]=ct
print("the words splitted are",words)
print(json.dumps(d,indent=1))
