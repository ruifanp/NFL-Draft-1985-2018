# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 16:21:36 2019

@author: Ruifan
"""
import math

def playerValueAvgGame(paYd, paTD, paInt, ruYd, ruTD, recYd, recTD, g, gs):
    passing = paYd/25.0 + paTD*4 - paInt*2
    rushing = ruYd/10.0 + 6*ruTD
    receiving = recYd/10.0 + 6*recTD
    longevity_multiplier = math.sqrt(g/16)
    
    if g == 0:
        return 0
    else:
        res = (passing + rushing + receiving)/g * longevity_multiplier
        if res < 0:
            return 0
        else:
            return res


#print(playerValueAvgGame(30000, 180, 90, 2000, 8, 10, 1, 160, 158))