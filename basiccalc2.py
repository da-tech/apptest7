#basic calc to junior users
#Developer: Daniel Zambrano

#libraries#######
import os
#######



#funtion#######################################
def calc(x,y):
    suma = x + y
    print("La suma es: ", suma) 

#main#######################################
os.system("clear")
print ("Press number  1: ")
a = int input()

b = int input("Press number 2: ")
calc(a,b)