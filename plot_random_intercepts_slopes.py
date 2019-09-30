

### Aummary and plot of an analysis with random intercept / random intercept +  random slope for 1 parameter
### hue is the random intercept parameter for the plot

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import seaborn as sns
import matplotlib.pyplot as plt


### Plot of the random intercepts
def plot_rand_int(data, x, y, hue, summary=True): 
    pal = sns.color_palette("tab10", n_colors=len(list(data[hue].unique())), desat=1).as_hex()
    sns.lmplot(x, y, data,  hue=hue, hue_order=list(data[hue].unique()),
               fit_reg=False, legend=False, size=8, palette=pal)
    md = smf.mixedlm(y + '~' + x, data, groups=hue)
    mdf = md.fit()
    ### 
    intercept_add_each= np.array([mdf.random_effects[N][hue] for N in list(data[hue].unique())])
    slope = mdf.params[x]
    intercept_each_subj =  intercept_add_each + mdf.params.Intercept
    for i, ind in enumerate(list(data[hue].unique())):
        
        intercept_s=intercept_each_subj[i]
        start_l = data[x].min()
        end_l = data[x].max()
        plt.plot([start_l, end_l], [slope*start_l + intercept_s, slope*end_l + intercept_s], color=pal[i])
    #
    if summary==True:
        print(mdf.summary())




### Plot of the random slopes
def plot_rand_slope(data, x, y, hue, summary=True): 
    pal = sns.color_palette("tab10", n_colors=len(list(data[hue].unique())), desat=1).as_hex()
    sns.lmplot(x, y, data,  hue=hue, hue_order=list(data[hue].unique()),
               fit_reg=False, legend=False, size=8, palette=pal)
    md = smf.mixedlm(y + '~' + x, data, groups=hue, re_formula='~' + x)
    mdf = md.fit()
    ### 
    intercept_add_each= np.array([mdf.random_effects[N][hue] for N in list(data[hue].unique())])
    slope_each = np.array([mdf.random_effects[N][x] for N in list(data[hue].unique())])    
    intercept_each_subj =  intercept_add_each + mdf.params.Intercept
    slope_each_subj =  slope_each + mdf.params[x]
    #
    for i, ind in enumerate(list(data[hue].unique())):        
        intercept_s=intercept_each_subj[i]
        slope_s = slope_each_subj[i]
        start_l = data[x].min()
        end_l = data[x].max()
        plt.plot([start_l, end_l], [slope_s*start_l + intercept_s, slope_s*end_l + intercept_s], color=pal[i])
    #
    if summary==True:
        print(mdf.summary())





###


#Information about the theory of mixed liniar models (random slopes) in http://www.bristol.ac.uk/cmm/learning/videos/random-slopes.html
#Information to undertand regressions (lasso, simpson paradox..) in the notebook Dropbox/KAROLINSKA/Understanding_of_regressions.ipynb

