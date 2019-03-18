# Dot plot function

Example with 1

```
dotplot(df=df, columns='A_err', subjects='subject', colors='k', xnames='Cond1')
```

![](https://github.com/davidbestue/funciones/blob/master/download%20(1).png)





Example with 2

```
dotplot(df=df, columns=['A_err', 'A_err_abs' ], subjects='subject', colors=['r', 'g'], xnames=['cond1', 'Cond2'],
        title='Conditions plot', xlabel='', ylabel='value')
```


![](https://raw.githubusercontent.com/davidbestue/funciones/master/download.png)


# bootstrap.py

Generates the inf and superior confidence interval of an array. 
Commented you have an example of how to run it in parallel for multiple samples.

It is bootstrap with replacement. It takes an array of the same length of the original but there is going to be repeted measures.

It is suggested to put it into the site-pakeges folder

'C:\Users\David\Anaconda3\envs\python3\Lib\site-packages\bootstrap.py'


Simple example
```
from bootstrap import *

a = np.random.rand(1000)
n = bootstrap_repl(a, ci=95, n=1000, stat=np.mean)

print(n)
(0.4736973603664837, 0.5102396146145342)
```


Serie/ paralel example (paralel is suggested!)
```
As = [np.random.rand(1000) for i in range(0,100)]

#### Serie
n=[]
for a in As:
    n.append(bootstrap_repl(a))

print(n)
[(0.4736973603664837, 0.5102396146145342), (0.49254558510255847, 0.5286548899342883), ... , (0.4704919715461403, 0.5052919240356857)]


#### Paralel
numcores = multiprocessing.cpu_count()
n = Parallel(n_jobs = numcores)(delayed(bootstrap_repl)(a) for a in As)

print(n)
[(0.4736973603664837, 0.5102396146145342), (0.49254558510255847, 0.5286548899342883), ... , (0.4704919715461403, 0.5052919240356857)]
```

# Decode function

From an activity decodes the population vector

```
decode(RE)
```

Output is an angle 0-360 degrees. Negative values are computed as positive in the opposite quadrant (q1;q3, q2:q4)


# remove_outlier_mult_columns.py

Remove the otliers of many columns at the same time! From the initial dataframe)
Input a list with the names of the columns (Pandas dataFrame)
Output the dataframe without outliers.
