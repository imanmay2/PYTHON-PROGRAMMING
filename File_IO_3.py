#Multiplication table
for i in range(2,21):
    with open(f"Multiplication table of{i}.txt","w") as f:
        for j in range(1,11):
            f.write(f"{i}*{j}={i*j}\n")
    
