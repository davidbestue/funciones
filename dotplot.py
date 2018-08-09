

#Function to plot the General mean, the mean of the subjects and the ci respecting the subject level
#You input a pandas Dataframe

def dotplot(df, columns, subjects, dotsize=10, dotsizemin=5, colors='g', xnames='',
             title='', xlabel='', ylabel='', bootstrap_function_use = 'bootstrap_subjlevel_same_n'):
    #######################################################################################
    #######################################################################################
    import numpy as np
    import numpy.random as npr
    from numpy import array, mean, random
    import matplotlib.pyplot as plt
    from scikits.bootstrap import ci 
    
    #Change to list in case it is just one
    if isinstance(columns, str)==True:
        columns=[columns]
        xnames =[xnames]
    
    if isinstance(colors, str)==True:
        colors=[colors]
    
    #Function
    def bootstrap_subjlevel_same_n(df, col_int, indx_subj):
        data_grouped=df.groupby(indx_subj)
        sup, inf =     ci([data_grouped.get_group(i)[col_int].mean() for i in df[indx_subj].unique()])
        return sup, inf
    
    def bootstrap_subjlevel_diff_n(df, col_int, indx_subj):
      data_grouped=df.groupby(indx_subj)
      ci([data_grouped.get_group(i)[col_int].mean() for i in df[indx_subj].unique()])
      sup, inf =     ci([data_grouped.get_group(i)[col_int].mean() for i in df[indx_subj].unique()])
      return sup, inf
    
    if bootstrap_function_use == 'bootstrap_subjlevel_same_n'
      bootstrap_function = bootstrap_subjlevel_same_n
     elif bootstrap_function_use == 'bootstrap_subjlevel_diff_n':
      bootstrap_function = bootstrap_subjlevel_diff_n
      
    ########################################################################################
    ########################################################################################
    #Plot for each column
    for xpos, column in enumerate(columns):
        #Color
        if len(colors)>1:
            color=colors[xpos]
        else:
            color = colors[0]
        
        #Confidence interval subject
        sup, inf = bootstrap_function(df, column, subjects)
        errors=(   [abs(sup -df[column].mean())], [abs(df[column].mean() - inf)])

        #Plot
        plt.errorbar(xpos, df[column].mean(), yerr=errors, ecolor='k', alpha=0.4, fmt='o', capsize=2)
        plt.plot(xpos, df[column].mean(), color=color,marker = 'o', markersize=dotsize, alpha=1 )
        A=df.groupby([subjects])
        Means = [A.get_group(i)[column].mean() for i in list(df.subject.unique())]
        [plt.plot(xpos, Means[i], color=color, marker = 'o', markersize=dotsizemin, alpha=0.4 ) for i in range(len(Means))]
        ###
    
    #xticks
    if xnames!='':
        plt.xticks(list(range(0, len(columns))), xnames) 
    
    #features
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.title(title) if title!='' else plt.title('')
    plt.xlabel(xlabel) if title!='' else plt.xlabel('')
    plt.ylabel(ylabel) if title!='' else plt.ylabel('')
    plt.xlim(-3, xpos+3)
    plt.show(block=False)
