# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 10:09:09 2019

@author: David Bestue
"""

import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

def remove_outlier_mult_columns(df_in, col_names):
    ### column names is a list of the columns to remove outliers
    outliers_booleans = []
    for col_name in col_names:        
        q1 = df_in[col_name].quantile(0.25)
        q3 = df_in[col_name].quantile(0.75)
        iqr = q3-q1 #Interquartile range
        fence_low  = q1-1.5*iqr
        fence_high = q3+1.5*iqr
        #
        inf_outliers = df_in[col_name] < fence_low ## outliers = 1
        sup_outliers = df_in[col_name] > fence_high ## outliers = 1
        outliers_booleans.append ( inf_outliers + sup_outliers )
    
    outliers_bool = sum(outliers_booleans)
    outliers_bool[outliers_bool>=1] = 1
    print( 'number of outliers: ' + str(sum(outliers_bool)) )
    outliers_bool = outliers_bool == 0
    
    ###boxplots of outliers
    fig = plt.figure()
    fig.suptitle('Detection of outliers')
    pallete = sns.color_palette("viridis", n_colors=len(col_names), desat=1).as_hex()
    for idx,col_name in enumerate(col_names):
        ax1 = fig.add_subplot(1,len(col_names),idx+1)
        sns.boxplot(df_in[col_name], orient="h", ax=ax1, color=pallete[idx])
    
    ##
    plt.show(block=False)
    
    
    return df_in[outliers_bool]
    
    


