# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 15:02:28 2020

@author: Tobi Sizi
"""

import numpy as np

#I TOLD YOU NOT TO LOOK AT IT!!!!!!!!!!!!!!!!! please dont judge me for what i have done
#create function, that creates all possible combinations of a 3x3 lists with entries 0 and 1:
def list9():
    result=[]
    for a in [0,1]:
        for b in [0,1]:
            for c in [0,1]:
                for d in [0,1]:
                    for e in [0,1]:
                        for f in [0,1]:
                            for g in [0,1]:
                                for h in [0,1]:
                                    for i in [0,1]:
                                        result = result +  [[[[a,b,c],[d,e,f],[g,h,i]]]]
    return result
