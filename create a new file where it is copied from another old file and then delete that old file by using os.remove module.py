import os
old="sample.txt"
new="renamed-by-python.txt"
with open(old) as f:
    content=f.read()
with open(new,"w") as f1:
    f1.write(content)
os.remove(old)
