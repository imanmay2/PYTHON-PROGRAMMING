n=int(input("for how many multiplication table do you want"))
for i in range(1,n+1):
    with open(f"multiplication table of {i}.txt","w") as f:
        for j in range(1,11):
            f.write(f"{i}x{j}={i*j}\n")
            
