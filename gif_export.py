# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 23:50:12 2020

@author: Tobi Sizi
"""

import numpy as np


#cemu is faster that cdic is faster than cifs
import conways_solved_ala_emu as cemu

#to compare cdic and cifs
import timeit

#Specify board size N and number of steps M
M = 300
N = 120

#first we define some simple structures
Y, X = 40, 35
SQUARE = np.array([[1,1],
                   [1,1]])
GOSPER_LEFT = np.array([[0,0,1,1,0,0,0,0],
                        [0,1,0,0,0,1,0,0],
                        [1,0,0,0,0,0,1,0],
                        [1,0,0,0,1,0,1,1],
                        [1,0,0,0,0,0,1,0],
                        [0,1,0,0,0,1,0,0],
                        [0,0,1,1,0,0,0,0]])
GOSPER_RIGHT = np.array([[0,0,0,0,1],
                        [0,0,1,0,1],
                        [1,1,0,0,0],
                        [1,1,0,0,0],
                        [1,1,0,0,0],
                        [0,0,1,0,1],
                        [0,0,0,0,1]])
#now we can put the parts togehter
GOSPER_PARTS=[[SQUARE, Y+16, X+12], 
              [GOSPER_LEFT, Y+14, X+22], 
              [GOSPER_RIGHT, Y+12, X+32], 
              [SQUARE, Y+14, X+46]]
GOSPER = cemu.implementManyIntoZero(N, GOSPER_PARTS)

#for the simkin gun I need one more part
SIMKIN_PART = np.array([[0,0,1],
                        [1,1,1],
                        [1,0,1],
                        [1,0,0]])
#now we can put the simkin gun together
SIMKIN_PARTS = [[SQUARE, Y+11, X+11],
                [SQUARE, Y+11, X+18],
                [SQUARE, Y+14, X+15],
                [SQUARE, Y+19, X+38],
                [SQUARE, Y+22, X+35],
                [SQUARE, Y+22, X+42],
                [SIMKIN_PART, Y+11, X+29]]
SIMKIN = cemu.implementManyIntoZero(N, SIMKIN_PARTS)

#lets finally generate the random array
RANDOM = np.random.randint(2, size=(N,N))

#lets calculate the .gifs using cemu, since it is faster
cemu.exportAsGif(GOSPER, M, "Gopser_Gun")
cemu.exportAsGif(SIMKIN, M, "Simkin_Gun")
cemu.exportAsGif(RANDOM, M, "Random_Start")



