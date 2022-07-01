with open("donkey.txt") as f:
    data=f.read()
data=data.replace("DONKEY","**&&%%##@@")
with open("donkey.txt","w") as f:
    f.write(data)
