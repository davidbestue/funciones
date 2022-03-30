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
        resample = a[np.random.randint(0, len(a), len(a))] 
        sample.append(stat(resample))
    
    # c1
    c_inf = pd.DataFrame(np.array(sample)).quantile(     float(100-ci)/2 /100       ).loc[0]  ## 0.025
    c_sup = pd.DataFrame(np.array(sample)).quantile(   1 - (float(100-ci)/2) /100         ).loc[0] ## 0.975
    
    return c_inf, c_sup



### Another method that does the same (online)

import numpy as np
import numpy.random as npr
import pylab


def bootstrap(data, num_samples, statistic, alpha):
    """Returns bootstrap estimate of 100.0*(1-alpha) CI for statistic."""
    n = len(data)
    idx = npr.randint(0, n, (num_samples, n))
    samples = data[idx]
    stat = np.sort(statistic(samples, 1))
    return (stat[int((alpha/2.0)*num_samples)],
            stat[int((1-alpha/2.0)*num_samples)])


    
#

def boots_by_subj(data, col_int, col_subj, n_iterations, alpha, stat):
    #### you give a 2 column df, one column qith the value and the other column with subject index:
    list_subjects = data[col_subj].unique()
    sample=[]
    for n in range(n_iterations):
        resampled=[]
        new_sample = list(np.random.randint(0, len(list_subjects), len(list_subjects)))
        for res_s in new_sample:
            resampled = resampled + list(data.loc[data[col_subj]==list_subjects[res_s], col_int].values) 
        #
        sample.append(stat(resampled))
    #
    stats_sorted = np.sort(sample)
    new_mean=np.mean(sample)
    return (new_mean, stats_sorted[int((alpha/2.0)*n_iterations)],
            stats_sorted[int((1-alpha/2.0)*n_iterations)])


    
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







