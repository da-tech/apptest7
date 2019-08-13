#libraries################################
import os
#funtion####################################
def calc(x,y,z) :
    if z == 1 :
        Ans = x + y
    elif z == 2 :
        Ans = x - y 
    elif z == 3 :
        Ans = x * y
    else :
         Ans = x / y
    return Ans

#main#########################################
os.system("clear") 
n1 = int (input("first number: ")) 
n2 = int(input(second number))


