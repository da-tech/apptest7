#developer: dniel zambrano
#random 1 exercise
import os
from random import randint , uniform, random

#this function genretion los numbers ##########
def Z():
    AnsZ = randint (0,100)
    return AnsZ

#
def R():
     AnsR = uniform (0,100)
     return AnsR

#main#############
os.system("clear")
print("the integer random number is:",Z())
r = R()
print("the float random number is:", r)