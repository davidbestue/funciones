# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 12:26:52 2019

@author: David Bestue
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Rectangle
import scikits.bootstrap as bootstraps
from seaborn_sinaplot import sinaplot ## install at https://github.com/mparker2/seaborn_sinaplot
import numpy as np

   
def linares_plot(x, y, df, palette, order, hue=None, hue_order=None, point_size=1, alpha=0.4, width=0.6, statistic=np.mean):
    
    sinaplot.sinaplot(x=x, y=y, hue=hue, data=df, violin=False, point_size=point_size, palette=palette,
                      alpha=alpha, order=order, hue_order=hue_order, width=width)
    if hue==None:
        for i_x, x_idx in enumerate(order):
            ci= bootstraps.ci(df.groupby(x).get_group(x_idx)[y], statfunction=statistic, n_samples=10000)
            m= statistic( df.loc[df[x]==x_idx, y] )
            left = i_x - width/len(order) 
            plt.gca().add_patch(Rectangle((left, ci[0]), width, ci[1]-ci[0],alpha=1, fill=False, linewidth=1,
                                          edgecolor='black'))
            
            plt.plot([left, left+width], [m,m ], 'r', linewidth=1)
    else:
        for i_x, x_idx in enumerate(order):
            for i_h, h_idx in enumerate(hue_order):
                try:
                    ci= bootstraps.ci(dfr.groupby(x).get_group(x_idx).groupby(hue).get_group(h_idx)[y], 
                                      statfunction=statistic, n_samples=10000)
                    m= statistic( df.groupby(x).get_group(x_idx).groupby(hue).get_group(h_idx)[y] )
                    bar_length = width/len(hue_order) 
                    bott_left = i_x - width/2   + i_h*bar_length
                    plt.gca().add_patch(Rectangle((bott_left, ci[0]), bar_length , ci[1]-ci[0],
                                                  alpha=1, fill=False, linewidth=1, edgecolor='black'))

                    plt.plot( [bott_left, bott_left+bar_length], [m,m ], 'r', linewidth=1)
                    
                except:
                    IndexError
        
        plt.gca().legend(loc= 1, frameon=False)
        #
    plt.xticks(  np.arange(len(df[x].unique())) , order)
    plt.xlim(-0.5, len(df[x].unique())-0.5 )
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().get_xaxis().tick_bottom()
    plt.gca().get_yaxis().tick_left()
    

    
    
#linares_plot(x='order', y='interference', hue='delay', df= df, palette='viridis', 
#              order=[1,2], hue_order=[0.2, 7], point_size=1.5, alpha=0.4, width=0.6 )  
#plt.title('Order & Delay')
#plt.show(block=False)
