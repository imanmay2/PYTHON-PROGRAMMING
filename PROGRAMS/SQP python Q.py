# Write a method COUNTLINES() in python to read lines from the text file 'TESTFILE.TXT'  
# and display the lines which are not starting with any vowel.
def COUNTLINES():
    with open("TESTFILE.TXT") as f:
        v='aeiou'
        ct=0
        for i in f.readlines():
            if(i[0] in v):
                ct+=1
    return ct


