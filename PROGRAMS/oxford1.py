ox={
    "chaku":"knife",
    "ladki":"wood"
}
print(ox)
key=input("enter the key form the dictionary")
if(ox.get(key)==None):
    print("hey buddy the coresponding to the value of this key is not found in the dictionaty")
else:
    print("the corressponding value of the key is",ox.get(key))