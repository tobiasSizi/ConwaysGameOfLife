# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 14:26:44 2020

@author: Tobi Sizi
"""
import numpy as np
import dont_look_at_this_please_please_PLEASE as dont_flipping_look_at_it
import PIL
from PIL import Image
import copy

#I DID THE CALCULATIONS FOR THE TIME EVOLUTION IN 2 WAYS: THIS IS THE DICTIONARY WAY
#THIS WAY ONLY TAKES 2/3 THE TIME conway_solved_via_ifs.py TAKES


#the goal is to do the evolution via a dictonary rather then a lot of if's
#first a function, that makes the 3x3 square of bits into a decimal:
def checkNeighborsDezimal(i,j,evo,gen=-1):
    N = len(evo[0])
    return int(f"{int(evo[gen][i-1][j-1])}{int(evo[gen][i-1][j])}{int(evo[gen][i-1][(j+1)%N])}{int(evo[gen][i][j-1])}{int(evo[gen][i][j])}{int(evo[gen][i][(j+1)%N])}{int(evo[gen][(i+1)%N][j-1])}{int(evo[gen][(i+1)%N][j])}{int(evo[gen][(i+1)%N][(j+1)%N])}", 2)


#this function checks how many neighbors of a given point are alive
def checkNeighborsSum(i,j,evo,gen=-1):
    N = len(evo[0])
    return np.sum([evo[gen][i-1][j-1], evo[gen][i-1][j], evo[gen][i-1][(j+1)%N],
                   evo[gen][i][j-1], evo[gen][i][(j+1)%N],
                   evo[gen][(i+1)%N][j-1], evo[gen][(i+1)%N][j], evo[gen][(i+1)%N][(j+1)%N]])

#this function checks if a point i,j will be alive/dead in the next round
#we need this funcion to create a dictionary
def evaluateDeadAlive(i,j,evo,gen=-1):
    if evo[gen][i][j] == 0 and checkNeighborsSum(i,j,evo) != 3:
        return 0
    elif evo[gen][i][j] == 0 and checkNeighborsSum(i,j,evo) == 3:
        return 1
    elif evo[gen][i][j] == 1 and checkNeighborsSum(i,j,evo) < 2:
        return 0
    elif evo[gen][i][j] == 1 and (checkNeighborsSum(i,j,evo) == 2 or checkNeighborsSum(i,j,evo,gen) == 3):
        return 1
    elif evo[gen][i][j] == 1 and checkNeighborsSum(i,j,evo) > 3:
        return 0
    
#now we create all possible combinations of 3x3 array with 0 and 1 as entries


#now we can create a list which contains the rules!
rules = [0 for i in range(0,512)]
for i in dont_flipping_look_at_it.list9():
    rules[checkNeighborsDezimal(1,1,i)] = evaluateDeadAlive(1,1,i)
    
#now we can do a one step evolution:
def evaluateNextStepWithCheck(evo,gen=-1):
    control = evo[-2]-evo[-1]
    n = len(evo[0])
    result = copy.deepcopy(evo[-1])
    for i in range(len(evo[0])):
        for j in range(len(evo[0])):
            if int(control[i][j]) != 0:
                result[i-1][j-1] = rules[checkNeighborsDezimal(i-1,j-1,evo)]
                result[i-1][j] = rules[checkNeighborsDezimal(i-1,j,evo)]
                result[i-1][(j+1)%n] = rules[checkNeighborsDezimal(i-1,(j+1)%n,evo)]
                result[i][j-1] = rules[checkNeighborsDezimal(i,j-1,evo)]
                result[i][j] = rules[checkNeighborsDezimal(i,j,evo)]
                result[i][(j+1)%n] = rules[checkNeighborsDezimal(i,(j+1)%n,evo)]
                result[(i+1)%n][j-1] = rules[checkNeighborsDezimal((i+1)%n,j-1,evo)]
                result[(i+1)%n][j] = rules[checkNeighborsDezimal((i+1)%n,j,evo)]
                result[(i+1)%n][(j+1)%n] = rules[checkNeighborsDezimal((i+1)%n,(j+1)%n,evo)]
    
    return np.append(evo, np.array([result]), axis=0)

def evaluateNextStepWOCheck(evo,gen=-1):
    result = np.zeros((len(evo[0]),len(evo[0])))
    for i in range(len(evo[0])):
        for j in range(len(evo[0])):
            result[i][j] = rules[checkNeighborsDezimal(i,j,evo)]
    return result

#the evolution will be done via recursion
def _evolution(evo, num_of_steps, carry):
    print(carry)
    if carry == num_of_steps:
        return evo
    else:
        return _evolution(evaluateNextStepWithCheck(evo), num_of_steps, carry+1)
    
def evolution(start_array, num_of_steps):
    carry=0
    evo = np.array([start_array, evaluateNextStepWOCheck([start_array])])
    return _evolution(evo, num_of_steps, carry)
#IT WORKS YAAAAAAAAAY


#I also want an implement function, that implements smaller structures into a bigger array
def implement(i,j, root, structure):
    for n in range(len(structure)):
        for m in range(len(structure[0])):
            root[n+i][m+j]=structure[n][m]
    return root
#AAAAND it works as well
    
def implementManyIntoZero(N, triple_list):
    result = np.zeros((N,N))
    for i in triple_list:
        result = implement(i[1], i[2],result, i[0])
    return result

#this function exports the array of evolution as .gif  ... FINALLY
def exportAsGif(start_array, number_of_steps, filename):
    images = []
    life = evolution(start_array, number_of_steps)
    for i in range(len(life)):
        images = images + [PIL.Image.fromarray(np.uint8(np.kron(life[i], np.ones((8,8)))*255))]
    images[0].save(f'{filename}.gif', append_images=images[1:], save_all=True,  optimize=True, duration=50, loop=1)
    print("GIF has been saved ... somewhere")
   

print("Rules have been established successfully")