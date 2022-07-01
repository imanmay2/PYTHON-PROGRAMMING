# to print the frequency of a word given by the user and print in the python shell
word=input("Enter any word you want")
ct=0
with open("copy.txt") as f:
    data=f.read().split()
    for i in data:
        if(i==word):
            ct+=1
print(f"The frequency of the {word} is {ct}")
    
