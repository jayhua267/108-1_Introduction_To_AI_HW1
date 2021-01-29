from functions import func
import array as arr
import numpy as np
import random
import math
from datetime import datetime

file1 = open('input.txt', 'r').read() 
lstfile = file1.split("\n")
print(lstfile)
RangeX  = lstfile[0].split(",")
RangeY = lstfile[1].split(",")


def  Brute_Force():
    minvalue = func(int(RangeX[0]) , int(RangeY[0]))
    j = 0
    for x in range(int(RangeX[0]),int(RangeX[1])):
        for y in range(int(RangeY[0]),int(RangeY[1])):
            ans = func(x,y)
            j = j + 1
            if minvalue > ans:
                minvalue = ans
                PosOfX = x
                PosOfY = y
    print("Brute Force's answer = ", round(minvalue,3), ", X = " , PosOfX , ",  Y = ", PosOfY,", Number Of Case = ", j )

def Anneal_Sim():
    #initial state     
    Temp = 2000
    CoolRate = 1 
    j = 0
    Flag = func((int(RangeX[0])+int(RangeX[1])) / 2 , (int(RangeY[0])+int(RangeY[1])) /2)
    RanX = random.randrange(int(RangeX[0]),int(RangeX[1]))
    RanY = random.randrange(int(RangeY[0]),int(RangeY[1]))
    Current = func(RanX,RanY)
    while Temp > 0 : 
    #Nei 
        NeiX = random.randrange(int(RangeX[0]),int(RangeX[1]))
        NeiY = random.randrange(int(RangeY[0]),int(RangeY[1]))
        RandNei = func(NeiX, NeiY)

    #Algorithm
        DeltaE = RandNei - Current
        if DeltaE < 0:
            RanX = NeiX
            RanY = NeiY
            Current = RandNei
        else :
            Prob = math.exp( DeltaE / Temp )
            if  Prob < random.uniform(0, 1) :
                RanX = NeiX
                RanY = NeiY
                Current = RandNei   
        Temp = Temp - CoolRate    
        j = j + 1
    print("Annealing Simulation's answer = ", round(Current,3), " , X = " , RanX , ",  Y = ", RanY,", Number Of Case = ", j )
 
if __name__=='__main__':
    tstart = datetime.now()
    Brute_Force()
    tend = datetime.now()
    print("Process time of Brute Force: ", (tend - tstart) )
    tstart = datetime.now()
    Anneal_Sim()
    tend = datetime.now()
    print("Process time of Annealing: ", (tend - tstart))
