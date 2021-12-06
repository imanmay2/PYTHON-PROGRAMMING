# wap to accept a sentence and count the frequency of each letter and print in the dictionary.

sen=input("enter the sentence you want to").lower()
alp_di="abcdefghijklmnopqruvwxyz1234567890"
fre={}
for i in sen:
    if i in alp_di:
        fre[i]=fre[i]+1
    else:
        fre[i]=1
print("........UPDATED DICTIONARY IS........")
print(fre)
