# Question to copy a file to a new one.

import os
with open("hello.txt") as f:
    data=f.read()
with open("copy.txt","w") as f1:
    f1.write(data)
os.remove("hello.txt")
    
    
    
    
