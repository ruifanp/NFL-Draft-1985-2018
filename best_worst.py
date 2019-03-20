# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 18:23:36 2019

@author: Ruifan
"""
import pandas as pd
from position_value_by_round import dfQB, dfRB, dfWR

df_offense = pd.concat([dfQB, dfRB, dfWR])

df_offense_top10 = df_offense[df_offense['Pick'] <= 10]
df_offense_late_rnd = df_offense[df_offense['Rnd'] >= 4]

print(df_offense_top10.sort_values(by = ['z_score'], ascending = True).head(14))
print(df_offense_late_rnd.sort_values(by = ['z_score'], ascending = False).head(10))
#print(df_offense.sort_values(by = ['z_score'], ascending = False).head(20))