# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 19:29:17 2019

@author: Ruifan
"""

import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib.ticker import FormatStrFormatter




pd.set_option('display.max_columns', 500)
df = pd.read_csv('NFL_draft_1985_2018.csv', encoding = "ISO-8859-1")
###Years prior to 1994 had 7+ round drafts. Remove rounds 8 and later with the assumption that those players would be undrafted Free agents###
df = df[df['Rnd'] <= 7]

replacements = [
    (['T', 'G', 'C'], 'OL'),
    (['OLB', 'DE'], 'Edge'),
    (['CB', 'S'], 'DB'),
    (['NT', 'DL'], 'DT')
]

for i in replacements:
    df['Pos'].replace(to_replace = i[0], value = i[1], inplace = True)

rnd_one_overall = df[df['Rnd'] == 1].count()['Player']/len(df)
#print('Percentage total players drafted in first round: {value:.2%}'.format(value=rnd_one_overall))

def compute_position(df, position):
    df1 = df[(df['Year'] >= 1985) & (df['Year'] <= 1993)]
    df2 = df[(df['Year'] >= 1994) & (df['Year'] <= 2002)]
    df3 = df[(df['Year'] >= 2003) & (df['Year'] <= 2011)]
    df4 = df[(df['Year'] >= 2012) & (df['Year'] <= 2018)]

    # position drafted over total players drafted
    pct_overall = df[df['Pos'] == position].count()['Player'] / len(df)
    count1 = df1[df1['Pos'] == position].count()['Player'] / len(df1)
    count2 = df2[df2['Pos'] == position].count()['Player'] / len(df2)
    count3 = df3[df3['Pos'] == position].count()['Player'] / len(df3)
    count4 = df4[df4['Pos'] == position].count()['Player'] / len(df4)

    print('Percentage of drafted players who are {pos}: {value:.2%}'.format(pos=position, value=pct_overall))
    print('Percentage of drafted players who are {pos} 1985-1993: {value:.2%}'.format(pos=position, value=count1))
    print('Percentage of drafted players who are {pos} 1994-2002: {value:.2%}'.format(pos=position, value=count2))
    print('Percentage of drafted players who are {pos} 2003-2011: {value:.2%}'.format(pos=position, value=count3))
    print('Percentage of drafted players who are {pos} 2012-2018: {value:.2%}'.format(pos=position, value=count4))

    # position drafted in first round over total position drafted
    pos_rnd_one_overall = df[(df['Pos'] == position) & (df['Rnd'] == 1)].count()['Player']/df[df['Pos'] == position].count()['Player']
    print('Percentage of {pos} drafted in first round: {value:.2%}'.format(pos=position, value=pos_rnd_one_overall))

    rnd_one_count1 = df1[(df1['Pos'] == position) & (df1['Rnd'] == 1)].count()['Player']/df1[df1['Pos'] == position].count()['Player']
    rnd_one_count2 = df2[(df2['Pos'] == position) & (df2['Rnd'] == 1)].count()['Player']/df2[df2['Pos'] == position].count()['Player']
    rnd_one_count3 = df3[(df3['Pos'] == position) & (df3['Rnd'] == 1)].count()['Player']/df3[df3['Pos'] == position].count()['Player']
    rnd_one_count4 = df4[(df4['Pos'] == position) & (df4['Rnd'] == 1)].count()['Player']/df4[df4['Pos'] == position].count()['Player']
    print('Percentage of {pos} drafted in first round 1985-1993: {value:.2%}'.format(pos=position, value=rnd_one_count1))
    print('Percentage of {pos} drafted in first round 1994-2002: {value:.2%}'.format(pos=position, value=rnd_one_count2))
    print('Percentage of {pos} drafted in first round 2003-2011: {value:.2%}'.format(pos=position, value=rnd_one_count3))
    print('Percentage of {pos} drafted in first round 2012-2018: {value:.2%}'.format(pos=position, value=rnd_one_count4))
    print('\n')
    
    return count1, count2, count3, count4, rnd_one_count1, rnd_one_count2, rnd_one_count3, rnd_one_count4


#qbs_by_era = compute_position(df, 'QB')
#rbs_by_era = compute_position(df, 'RB')
#wrs_by_era = compute_position(df, 'WR')
#tes_by_era = compute_position(df, 'TE')
#ols_by_era = compute_position(df, 'OL')
#edges_by_era = compute_position(df, 'Edge')
#dts_by_era = compute_position(df, 'DT')
#lbs_by_era = compute_position(df, 'LB')
#dbs_by_era = compute_position(df, 'DB')

########Plot the interesting results########################################################################################################################################
###Interesting positions (which have undergone change in relative draft value in 30 years) are QB, RB, Edge, and LB.########################################################
############################################################################################################################################################################


years = [i for i in range(1985, 2019)]
eras = ['1985-1993', '1994-2002', '2003-2011', '2012-2018']
lQBpct_overall = []
lQBfirstPct = []
lRBpct_overall = []
lRBfirstPct = []
lEdgepct_overall = []
lEdgefirstPct = []
lLBpct_overall = []
lLBfirstPct = []

for i in range(1985, 2019):
    num_drafted = df[df['Year'] == i].count()['Player']
    
    ###QBs###
    qbs_drafted = df[(df['Year'] == i) & (df['Pos'] == 'QB')].count()['Player']
    qbs_drafted_firstrnd = df[(df['Year'] == i) & (df['Pos'] == 'QB') & (df['Rnd'] == 1)].count()['Player']
    lQBpct_overall.append(qbs_drafted/num_drafted)
    lQBfirstPct.append(qbs_drafted_firstrnd/qbs_drafted)
    
    ###RBs###
    rbs_drafted = df[(df['Year'] == i) & (df['Pos'] == 'RB')].count()['Player']
    rbs_drafted_firstrnd = df[(df['Year'] == i) & (df['Pos'] == 'RB') & (df['Rnd'] == 1)].count()['Player']
    lRBpct_overall.append(rbs_drafted/num_drafted)
    lRBfirstPct.append(rbs_drafted_firstrnd/rbs_drafted)
    
    ###Edges###
    Edges_drafted = df[(df['Year'] == i) & (df['Pos'] == 'Edge')].count()['Player']
    Edges_drafted_firstrnd = df[(df['Year'] == i) & (df['Pos'] == 'Edge') & (df['Rnd'] == 1)].count()['Player']
    lEdgepct_overall.append(Edges_drafted/num_drafted)
    lEdgefirstPct.append(Edges_drafted_firstrnd/Edges_drafted)
    
    ###LBs###
    LBs_drafted = df[(df['Year'] == i) & (df['Pos'] == 'LB')].count()['Player']
    LBs_drafted_firstrnd = df[(df['Year'] == i) & (df['Pos'] == 'LB') & (df['Rnd'] == 1)].count()['Player']
    lLBpct_overall.append(LBs_drafted/num_drafted)
    lLBfirstPct.append(LBs_drafted_firstrnd/LBs_drafted)
    
###QBs all years
#fig, ax1 = plt.subplots()
#ax1.set_title('QBs drafted by year')
#ax1.set_xlabel('Year')
#ax1.set_ylabel('Proportion of drafted players who are QBs', color='black')
#ax1.scatter(years, lQBpct_overall, color='black')
#ax1.tick_params(axis ='y', labelcolor = 'black')
#
#ax2 = ax1.twinx()
#ax2.set_ylabel('Proportion of QBs drafted in 1st round', color='red' )
#ax2.scatter(years, lQBfirstPct, color='red')
#ax2.tick_params(axis ='y', labelcolor = 'red')
#plt.savefig('QBs_drafted_by_year')
#plt.show()

###QBs by era
#fig, ax1 = plt.subplots()
#ax1.set_title('QBs by era')
#ax1.set_xlabel('Era')
#ax1.set_ylabel('Proportion of drafted players who are QBs', color='black')
#ax1.plot(eras, [qbs_by_era[0], qbs_by_era[1], qbs_by_era[2], qbs_by_era[3]], color='black')
#ax1.set_ylim([0.04, 0.06])
#ax1.tick_params(axis ='y', labelcolor = 'black')
#
#ax2 = ax1.twinx()
#ax2.set_ylabel('Proportion of QBs drafted in 1st round', color='red' )
#ax2.plot(eras, [qbs_by_era[4], qbs_by_era[5], qbs_by_era[6], qbs_by_era[7]], color='red')
#ax2.tick_params(axis ='y', labelcolor = 'red')
#plt.savefig('QBs_drafted_by_era')
#plt.show()

###RBs all years
#fig, ax1 = plt.subplots()
#ax1.set_title('RBs drafted by year')
#ax1.set_xlabel('Year')
#ax1.set_ylabel('Proportion of drafted players who are RBs', color='black')
#ax1.scatter(years, lRBpct_overall, color='black')
#ax1.tick_params(axis ='y', labelcolor = 'black')
#
#ax2 = ax1.twinx()
#ax2.set_ylabel('Proportion of RBs drafted in 1st round', color='red' )
#ax2.scatter(years, lRBfirstPct, color='red')
#ax2.tick_params(axis ='y', labelcolor = 'red')
#plt.savefig('RBs_drafted_by_year')
#plt.show()
#
###RBs by era
#fig, ax1 = plt.subplots()
#ax1.set_title('RBs by era')
#ax1.set_xlabel('Era')
#ax1.set_ylabel('Proportion of drafted players who are RBs', color='black')
#ax1.plot(eras, [rbs_by_era[0], rbs_by_era[1], rbs_by_era[2], rbs_by_era[3]], color='black')
#ax1.tick_params(axis ='y', labelcolor = 'black')
#
#ax2 = ax1.twinx()
#ax2.set_ylabel('Proportion of RBs drafted in 1st round', color='red' )
#ax2.plot(eras, [rbs_by_era[4], rbs_by_era[5], rbs_by_era[6], rbs_by_era[7]], color='red')
#ax2.tick_params(axis ='y', labelcolor = 'red')
#plt.savefig('RBs_drafted_by_era')
#plt.show()

###Edges all years
#fig, ax1 = plt.subplots()
#ax1.set_title('Edges drafted by year')
#ax1.set_xlabel('Year')
#ax1.set_ylabel('Proportion of drafted players who are Edges', color='black')
#ax1.scatter(years, lEdgepct_overall, color='black')
#ax1.tick_params(axis ='y', labelcolor = 'black')
#
#ax2 = ax1.twinx()
#ax2.set_ylabel('Proportion of Edges drafted in 1st round', color='red' )
#ax2.scatter(years, lEdgefirstPct, color='red')
#ax2.tick_params(axis ='y', labelcolor = 'red')
#plt.savefig('Edges_drafted_by_year')
#plt.show()
##
###Edges by era
#fig, ax1 = plt.subplots()
#ax1.set_title('Edges by era')
#ax1.set_xlabel('Era')
#ax1.set_ylabel('Proportion of drafted players who are Edges', color='black')
#ax1.plot(eras, [edges_by_era[0], edges_by_era[1], edges_by_era[2], edges_by_era[3]], color='black')
#ax1.tick_params(axis ='y', labelcolor = 'black')
#
#ax2 = ax1.twinx()
#ax2.set_ylabel('Proportion of edges drafted in 1st round', color='red' )
#ax2.plot(eras, [edges_by_era[4], edges_by_era[5], edges_by_era[6], edges_by_era[7]], color='red')
#ax2.tick_params(axis ='y', labelcolor = 'red')
#plt.savefig('Edges_drafted_by_era')
#plt.show()

###LBs all years
#fig, ax1 = plt.subplots()
#ax1.set_title('LBs drafted by year')
#ax1.set_xlabel('Year')
#ax1.set_ylabel('Proportion of drafted players who are LBs', color='black')
#ax1.scatter(years, lLBpct_overall, color='black')
#ax1.tick_params(axis ='y', labelcolor = 'black')
#
#ax2 = ax1.twinx()
#ax2.set_ylabel('Proportion of LBs drafted in 1st round', color='red' )
#ax2.scatter(years, lLBfirstPct, color='red')
#ax2.tick_params(axis ='y', labelcolor = 'red')
#ax2.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
#plt.savefig('LBs_drafted_by_year')
#plt.show()
#
###LBs by era
#fig, ax1 = plt.subplots()
#ax1.set_title('LBs by era')
#ax1.set_xlabel('Era')
#ax1.set_ylabel('Proportion of drafted players who are LBs', color='black')
#ax1.plot(eras, [lbs_by_era[0], lbs_by_era[1], lbs_by_era[2], lbs_by_era[3]], color='black')
#ax1.tick_params(axis ='y', labelcolor = 'black')
#
#ax2 = ax1.twinx()
#ax2.set_ylabel('Proportion of LBs drafted in 1st round', color='red' )
#ax2.plot(eras, [lbs_by_era[4], lbs_by_era[5], lbs_by_era[6], lbs_by_era[7]], color='red')
#ax2.tick_params(axis ='y', labelcolor = 'red')
#ax2.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
#plt.savefig('LBs_drafted_by_era')
#plt.show()




































