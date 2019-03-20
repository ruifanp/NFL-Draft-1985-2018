# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 16:16:56 2019

@author: Ruifan
"""

import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt

from draft_frequency_by_position import df
from fcns import playerValueAvgGame


###Fill in NaN stats with 0
toFill = ['G', 'GS', 'QBrec', 'Cmp', 'PaAtt', 'PaYds', 'PaTD', 'PaInt', 'RuAtt', 'RuYds', 'RuTD', 'Rec', 'RecYds', 'RecTD', 'Int', 'Sk' ]
for i in toFill:
    df[i] = df[i].fillna(0)

###Populate player value column
df['playerValue'] = df.apply(lambda row: playerValueAvgGame(row['PaYds'], row['PaTD'], row['PaInt'], row['RuYds'], row['RuTD'], row['RecYds'], row['RecTD'], 
  row['G'], row['GS']), axis = 1)

##Divide into respective positions
dfQB = df[df['Pos'] == 'QB']
dfQB1 = df[(df['Pos'] == 'QB') & (df['Year'] >= 1985) & (df['Year'] <= 1993)]
dfQB2 = df[(df['Pos'] == 'QB') & (df['Year'] >= 1994) & (df['Year'] <= 2002)]
dfQB3 = df[(df['Pos'] == 'QB') & (df['Year'] >= 2003) & (df['Year'] <= 2011)]
dfQB4 = df[(df['Pos'] == 'QB') & (df['Year'] >= 2012) & (df['Year'] <= 2018)]

dfRB = df[df['Pos'] == 'RB']
dfRB1 = df[(df['Pos'] == 'RB') & (df['Year'] >= 1985) & (df['Year'] <= 1993)]
dfRB2 = df[(df['Pos'] == 'RB') & (df['Year'] >= 1994) & (df['Year'] <= 2002)]
dfRB3 = df[(df['Pos'] == 'RB') & (df['Year'] >= 2003) & (df['Year'] <= 2011)]
dfRB4 = df[(df['Pos'] == 'RB') & (df['Year'] >= 2012) & (df['Year'] <= 2018)]

dfWR = df[df['Pos'] == 'WR']
dfWR1 = df[(df['Pos'] == 'WR') & (df['Year'] >= 1985) & (df['Year'] <= 1993)]
dfWR2 = df[(df['Pos'] == 'WR') & (df['Year'] >= 1994) & (df['Year'] <= 2002)]
dfWR3 = df[(df['Pos'] == 'WR') & (df['Year'] >= 2003) & (df['Year'] <= 2011)]
dfWR4 = df[(df['Pos'] == 'WR') & (df['Year'] >= 2012) & (df['Year'] <= 2018)]




def getPlayerZScore(df):
    stdev = df['playerValue'].std()
    mean = df['playerValue'].mean()
    df['z_score'] = (df['playerValue'] - mean)/stdev
    return;
    
###Populates player z score column   
for i in [dfQB, dfQB1, dfQB2, dfQB3, dfQB4, dfRB, dfRB1, dfRB2, dfRB3, dfRB4, dfWR, dfWR1, dfWR2, dfWR3, dfWR4]:
    getPlayerZScore(i)


def avgZScore(df, rnd):
    df_rnd = df[df['Rnd'] == rnd]
    return df_rnd['z_score'].mean()

#print("Overall for QBs, RBs, and WRs")
#for i in [dfQB, dfRB, dfWR]:
#    for j in range(1,8):
#        print('Z-score for player chosen in round {}: {}'.format(j, avgZScore(i, j)))
#print('\n')
#
#print("QBs, starting from the most recent era")
#for i in [dfQB4, dfQB3, dfQB2, dfQB1]:
#    for j in range(1,8):
#        print('Z-score for player chosen in round {}: {}'.format(j, avgZScore(i, j)))
#print('\n')
#
#print("RBs, starting from the most recent era")
#for i in [dfRB4, dfRB3, dfRB2, dfRB1]:
#    for j in range(1,8):
#        print('Z-score for player chosen in round {}: {}'.format(j, avgZScore(i, j)))
#print('\n')
#       
#print("WRs, starting from the most recent era")
#for i in [dfWR4, dfWR3, dfWR2, dfWR1]:
#    for j in range(1,8):
#        print('Z-score for player chosen in round {}: {}'.format(j, avgZScore(i, j)))
#        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        