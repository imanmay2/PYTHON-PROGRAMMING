# Write a function that reads a file and display the words separated with #
def hass():
    file=input("Enter the file name")
    with open(file) as f:
        li=f.read().split()
        for i in li:
            if(i!=li[len(li)-1]):
                print(i,end='#')
            else:
                print(i)
hass()        


# copy text of one file to another and repeated space should be replaced by the single one  using def fucntions.
def hello():
    F=input("Enter the file name to copy from: ")
    f=input("Enter the file name to be pasted simultaneously: ")
    with open(F) as k:
        li=k.read().split()
        with open(f,"w") as K:
            for  i in li:
                K.write(i+" ")

hello()