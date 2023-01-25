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
# print("The number of lines not starting with any vowels: ",COUNTLINES())




# Write a function ETCount() in Python, which should read each character of a text file "TESTFILE.TXT" and then
# count and display the count of occurence of alphabets E and T insividually (including the small cases e and t too)
def ETCount():
    with open("TEST.TXT",'w') as f1:
        str2='Today is a pleasant day It might rain rain today It is mentioned on weather sites.'
        f1.write(str2)
    with open("TEST.TXT",'r') as f2:
        ct_t=0
        ct_e=0
        for i in f2.read():
            if(i=='e' or i=='E'):
                ct_e+=1
            elif(i=='t' or i=='T'):
                ct_t+=1
    print("E or e: ",ct_e)
    print("T or t: ",ct_t)
#ETCount()