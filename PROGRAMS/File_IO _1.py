f=open("poem.txt")
data=f.read().lower()
if("twinkle" in data):
    print("Twinkle is present in the file")
else:
    print("Twinkle is not present")
f.close()
