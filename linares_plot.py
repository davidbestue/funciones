# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:26:52 2019

@author: David
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Rectangle
import scikits.bootstrap as bootstraps
from seaborn_sinaplot import sinaplot ## install at https://github.com/mparker2/seaborn_sinaplot
import numpy as np

   
    
def linares_plot(x, y, df, pallete, order, hue=None, hue_order=None, point_size=1, alpha=0.4, width=0.6 ):
    
    sinaplot.sinaplot(x=x, y=y, hue=hue, data=df, violin=False, point_size=point_size, palette=pallete,
                      alpha=alpha, order=order, hue_order=hue_order, width=width)
    if hue==None:
        for i_x, x_idx in enumerate(order):
            ci = df.groupby(x)[y].apply(lambda n:bootstraps.ci(data=n.values)).iloc[i_x]
            
            left = i_x - width/2 
            plt.gca().add_patch(Rectangle((left, ci[0]), width, ci[1]-ci[0],alpha=1, fill=False, linewidth=1,
                                          edgecolor='black'))
            m = df.loc[df[x]==x_idx, y].mean()
            plt.plot([left, left+width], [m,m ], 'r', linewidth=1)
    else:
        for i_x, x_idx in enumerate(order):
            for i_h, h_idx in enumerate(hue_order):
                ci = df.groupby(x).get_group(x_idx).groupby(hue)[y].apply(lambda n:bootstraps.ci(data=n.values)).iloc[i_h]
                if i_h==0:
                    bott_left = i_x - width/2
                else:
                    bott_left = i_x 
                 
                bar_length = width/2 # 0.6/len(df[hue].unique())
                plt.gca().add_patch(Rectangle((bott_left, ci[0]), bar_length , ci[1]-ci[0],
                                              alpha=1, fill=False, linewidth=1, edgecolor='black'))
                
                m = df.loc[(df[x]==x_idx) & (df[hue]==h_idx) , y].mean()                
                plt.plot( [bott_left, bott_left+bar_length], [m,m ], 'r', linewidth=1)
        
        plt.gca().legend(loc= 1, frameon=False)
        #
    plt.xticks(  np.arange(len(df[x].unique())) , order)
    plt.xlim(-0.5, len(df[x].unique())-0.5 )
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().get_xaxis().tick_bottom()
    plt.gca().get_yaxis().tick_left()
    
    

    
    
#linares_plot(x='order', y='interference', hue='delay', df= df, pallete='viridis', 
#              order=[1,2], hue_order=[0.2, 7], point_size=1.5, alpha=0.4, width=0.6 )  
#plt.title('Order & Delay')
#plt.show(block=False)
