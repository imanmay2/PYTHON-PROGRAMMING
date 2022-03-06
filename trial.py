import math
def terrace(userNum1,userNum2):
    temp1, temp2 = userNum1, userNum2
    gcd = math.gcd(temp1, temp2)
    li = [2, 3, 5, 7, 11, 13, 17, 19]
    i = 0
    while True:
        if(userNum1 % li[i] == 0 and userNum2 % li[i] == 0):
            userNum1, userNum2 = userNum1//li[i], userNum2//li[i]
            i = 0
            lis1 = list(str(userNum1))
            lis2 = list(str(userNum2))
            z, k = 0, 0
            if len(lis1) == len(lis2):
                for z in lis1:
                    if(z in lis2):
                        k += 1
                for z in lis2:
                    if(z in lis2):
                        k += 1
                if(k == len(lis1)*2):
                    if(temp1//gcd == temp2//gcd -1 or temp1//gcd == temp2//gcd+1):
                        return True
                    else:
                        return False
        elif(userNum1 < 1 or userNum2 < 1 or i == len(li)-1):
            return False
        else:
            i += 1

n=int(input("enter 1:"))
n2=int(input("enter 2 :"))
print(terrace(n,n2))
