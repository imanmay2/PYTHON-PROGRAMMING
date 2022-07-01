# program to create a dictionary of finding the frequency of a senetence
word=input("Enter a sentence of more than 4 words")
li=word.split()
d={}
for i in li:
    if(i not in d):
        ct=li.count(i)
        d[i]=ct
print("Dictionary created is as follows")
print(d)
