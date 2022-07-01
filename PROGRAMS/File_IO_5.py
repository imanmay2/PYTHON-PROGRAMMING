content=True
i=1
word=input("Enter the word to be searched")
with open("sample.txt") as f:
    while content:
        content=f.readline()
        if(word in content.lower()):
            print(content)
            print(f"Yes {word} is present in the line number {i}")
        i=i+1
