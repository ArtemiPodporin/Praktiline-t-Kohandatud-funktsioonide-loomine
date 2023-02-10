from math import *
from random import *
from OmaModul import *

#12
vastus=arithmetic(float(input("arv1:")),input("tehe:"),float(input("arv2:")))

#1
def arithmetic(arc1:float,tehe:str,arv2:float)->:
    """
    mis võtab 3 argumenti: esimesed 2 on nadrad, kolmas on nendega tehtav operatsioon. Kui kolmas argument on +, sisestage need; if - siis lahuta; * - korrutada; / - lõhestamine (esimene kaheks). Muudel juhtudel tagastage string "Tundmatu toiming"
    """
    if tehe=="+":
        vastus=arv1+arv2
    elif tehe=="-":
        vastus=arv1-arv2
    elif tehe=="*":
        vastus=arv1*arv2
    elif tehe=="/":
        if arv2==0:
            vastus="DIVO"
        else:
            vastus=arv1/arv2
    else:
        vastus="Tundatu tehe"

    return vastus

#2
def is_year_leap(aasta):
    if aasta % 4 == 0:
        if aasta % 100 == 0:
            if aasta % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
#3
import math

def square(side):
    perimeter = 4 * side
    area = side * side
    diagonal = math.sqrt(2 * side * side)
    return perimeter, area, diagonal


#4
def season(month):
    if month in [12, 1, 2]:
        return "talv"
    elif month in [3,4,5]:
        return "kevad"
    elif month in [6,7,8]:
        return "suvi"
    elif month in [9,8,7]:
        return "sügi"
    else:
        return "Invalid month number"
#5



#6
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%1==0:
            return False
        return True
#7
def is_valid_date(day, month, year):
    if month < 1 or month > 12:
        return False
    if day < 1 or day >31:
        return False
    if month in [4,6,9,11] and day >30:
        return False
    if month ==2:
        if day > 29:
            return False
        if day==29:
            if year % 4!=0 or (year%100==0 and year% 400 !=0):
                return False
#8
