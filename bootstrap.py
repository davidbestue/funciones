# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 17:10:13 2019

@author: David Bestue
"""

import pandas as pd
import numpy as np
from joblib import Parallel, delayed
import multiprocessing


def bootstrap_repl(a, ci=95, n=1000, stat=np.mean):
    # a must be an array
    # decide the confidence interval, default = 95%
    sample = []
    for i in range(n):
        resample = a[np.random.randint(1, len(a), len(a))] 
        sample.append(stat(resample))
    
    # c1
    c_inf = pd.DataFrame(np.array(sample)).quantile(     float(100-ci)/2 /100       ).loc[0]  ## 0.025
    c_sup = pd.DataFrame(np.array(sample)).quantile(   1 - (float(100-ci)/2) /100         ).loc[0] ## 0.975
    
    return c_inf, c_sup

    
#    
#
### Example
#As = [np.random.rand(1000) for i in range(0,100)]
#
#
#### serie
#n=[]
#for a in As:
#    n.append(bootstrap_repl(a))
#
#print(n)
#
#
#### paralel!
#numcores = multiprocessing.cpu_count()
#alltuns = Parallel(n_jobs = numcores)(delayed(bootstrap_repl)(a) for a in As)
#print(alltuns)
#







